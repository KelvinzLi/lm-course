#!/bin/bash
source assets/argparse.sh

define_arg "experiment" "default" "The experiment to run" "string" "optional"
define_arg "nodes" "1" "The number of nodes to use" "int" "optional"
define_arg "gpus_per_node" "1" "The number of GPUs per node to use" "int" "optional"
define_arg "cpus_per_node" "4" "The number of CPUs per node to use" "int" "optional"
define_arg "mem_per_node" "32G" "The amount of memory per node to use" "string" "optional"
define_arg "time" "120:00:00" "The time limit for the job" "string" "optional"
define_arg "sweep_start" "0" "The starting idx of the sweep list (if experiment is a sweep)" "string" "optional"
define_arg "sweep_end" "0" "The ending idx of the sweep list (if experiment is a sweep)" "string" "optional"

parse_args "$@"

mkdir -p log

sbatch <<EOF
#!/bin/bash
#SBATCH --job-name=$experiment
#SBATCH --output=log/%j_$experiment.out
#SBATCH --error=log/%j_$experiment.out
#SBATCH --nodes=$nodes
#SBATCH --ntasks-per-node=$gpus_per_node
#SBATCH --gres=gpu:H100:$gpus_per_node
#SBATCH --cpus-per-task=$cpus_per_node
#SBATCH --mem=$mem_per_node
#SBATCH --time=$time
#SBATCH --array=$sweep_start-$sweep_end

export SLURM_CPU_BIND=cores
export PYTHONUNBUFFERED=1

# Get master node
MASTER_ADDR=\$(scontrol show hostname \$SLURM_NODELIST | head -n 1)
MASTER_PORT=29500

echo "Launching \$SLURM_NTASKS tasks across \$SLURM_NNODES nodes"
echo "Master: \$MASTER_ADDR:\$MASTER_PORT"

# Export so srun tasks inherit them
export MASTER_ADDR
export MASTER_PORT

srun bash -c "
export WORLD_SIZE=\\\$SLURM_NTASKS
export RANK=\\\$SLURM_PROCID
export LOCAL_RANK=\\\$SLURM_LOCALID

echo \"Node: \\\$(hostname), Rank: \\\$RANK/\\\$WORLD_SIZE\"
echo \"MASTER_ADDR=\\\$MASTER_ADDR, MASTER_PORT=\\\$MASTER_PORT\"

uv --preview-features extra-build-dependencies run python -m lm.pretrain --experiment=$experiment --experiment_id=\\\$SLURM_ARRAY_TASK_ID
"
EOF
