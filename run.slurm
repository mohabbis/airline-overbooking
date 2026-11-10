#!/bin/bash
#SBATCH --job-name=airline-overbooking
#SBATCH --account=compfor203f26s001_class
#SBATCH --partition=standard
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH --time=00:05:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --error=logs/%x-%j.err

# Stop if a command fails
set -e

# Go to the project directory
cd "$SLURM_SUBMIT_DIR"

# Print job information
echo "Compute node: $(hostname)"
echo "Job ID: $SLURM_JOB_ID"

# Load and activate Mamba
module load mamba
eval "$(mamba shell hook --shell bash)"
mamba activate "$HOME/.conda/envs/airline-overbooking"

# Verify Python version
python --version

# Run the simulation
python simulation.py
