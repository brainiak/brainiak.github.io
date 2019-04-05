#!/usr/bin/env bash
# Input python command to be submitted as a job

#SBATCH --output=../generate_data-%j.out
#SBATCH --job-name generate_data
#SBATCH -t 30
#SBATCH -m=4G
#SBATCH -n 1

# Set up the environment
source ../setup_environment.sh

# Run the python script
python ./generate_data.py
