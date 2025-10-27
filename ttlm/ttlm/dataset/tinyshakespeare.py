"""PyTorch Dataset for sampling from a Parquet file."""

import polars as pl
from torch.utils.data import Dataset


class TinyShakespeare(Dataset):
    """
    A memory-scalable PyTorch Dataset for reading a Parquet file, designed to
    work efficiently with multiprocessing (num_workers > 0) in DataLoader.

    This dataset initializes lazily within each worker process to avoid sharing
    complex objects across processes, which can cause deadlocks. The main
    process only scans the dataset to get the total number of rows.
    """

    def __init__(
        self,
        parquet_path: str,
        text_column: str = "text",
        filter_column: str = "is_empty",
        filter_value: bool = False,
    ) -> None:
        """
        Initializes the dataset by storing metadata but defers reading data.

        Args:
            parquet_path: Path to the Parquet file.
            text_column: The name of the column containing the text data.
            filter_column: The name of the column to filter by.
            filter_value: The value to filter for in the filter_column.
        """
        super().__init__()
        self.parquet_path = parquet_path
        self.text_column = text_column
        self.filter_column = filter_column
        self.filter_value = filter_value

        # Perform a quick scan to get the number of valid rows without loading data.
        # This is fast and memory-efficient.
        self.num_valid_rows = (
            pl.scan_parquet(self.parquet_path)
            .filter(pl.col(self.filter_column) == self.filter_value)
            .select(pl.count())
            .collect()
            .item()
        )

        # These will be initialized lazily in each worker process.
        self.data = None

    def _init_data(self) -> None:
        """Initializes the data connection within the worker process."""
        # Eagerly load the filtered data into memory *within this worker*.
        # This is the key to making it scalable and avoiding deadlocks.
        self.data = (
            pl.read_parquet(self.parquet_path, memory_map=True)
            .filter(pl.col(self.filter_column) == self.filter_value)
            .select(self.text_column)
        )

    def __len__(self) -> int:
        """Returns the number of rows that satisfy the filter condition."""
        return self.num_valid_rows

    def __getitem__(self, idx: int) -> str:
        """
        Retrieves the 'text' sample for the idx-th valid row.

        Initializes the data connection on the first call within each worker.
        """
        if self.data is None:
            self._init_data()

        if not (0 <= idx < self.num_valid_rows):
            raise IndexError("Index out of range for the filtered dataset")

        # __getitem__ on a Polars DataFrame/Column is highly optimized.
        return self.data[self.text_column][idx]
