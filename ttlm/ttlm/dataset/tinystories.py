"""PyTorch Dataset for sampling from a Parquet file."""
import requests
from torch.utils.data import Dataset

class TinyStories(Dataset):
    """
    Tiny stories dataset (subset).
    """
    def __init__(
        self,
        url: str = "https://www.cs.toronto.edu/~cmaddis/files/TinyStories-train-subset.txt"
    ) -> None:
        """Initializes the dataset by storing metadata but defers reading data."""
        super().__init__()
        self.url = url
        self.data = self._init_data()

    def _init_data(self, url: str = "https://www.cs.toronto.edu/~cmaddis/files/TinyStories-train-subset.txt") -> list[str]:
        """Downloads the TinyStories text file and splits it into individual stories to create the dataset."""
        response = requests.get(url)
        response.raise_for_status()
        text = response.text
        stories = [story.strip() for story in text.split('<|endoftext|>') if story.strip()]
        return stories

    def __len__(self) -> int:
        """Returns the number of rows that satisfy the filter condition."""
        return len(self.data)

    def __getitem__(self, idx: int) -> str:
        """
        Retrieves the 'text' sample for the idx-th valid row.
        Initializes the data connection on the first call within each worker.
        """
        if not (0 <= idx < len(self.data)):
            raise IndexError("Index out of range for the dataset")
        return self.data[idx]
