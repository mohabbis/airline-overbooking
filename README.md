Airline Overbooking Simulation


1. Project Overview

This project uses a Python Monte Carlo simulation to explore how airline overbooking affects profitability.

The question I wanted to answer was: How many tickets should an airline sell for a 100-seat flight to maximize its expected profit?

Airlines sometimes sell more tickets than available seats because some passengers do not show up. While this increases revenue, it also creates the possibility of having to compensate passengers who cannot board.

My simulation uses the following assumptions:

100 available seats

$200 per ticket

10% probability that each passenger does not show up

$400 compensation for each bumped passenger

1,000 simulated flights per ticket quantity

Ticket quantities ranging from 100 to 120

Random seed of 42 for reproducibility

Profit is calculated as ticket revenue minus compensation for bumped passengers.

2. Reproducing the Project

The project uses Python 3.11 and Mamba.

Create and activate the environment:

mamba env create -f environment.yml
mamba activate airline-overbooking

Run the simulation:

python simulation.py

Run the tests:

python -m pytest -v

The project contains seven pytest tests covering profit calculations, edge cases, and random-seed reproducibility. All seven tests passed on Great Lakes.

Submit the SLURM job on Great Lakes:

The run.slurm script uses the COMPFOR 203 course allocation. On Great Lakes, create the environment at the path expected by the script:

module load mamba/py3.11
mamba env create -f environment.yml --prefix ~/.conda/envs/airline-overbooking
mkdir -p logs
sbatch run.slurm

The SLURM script specifies the course account, so anyone using a different allocation would need to update it.

My job ran successfully on Great Lakes:

Job ID: 65869603

Compute node: gl3025.arc-ts.umich.edu

Status: COMPLETED

Exit code: 0:0

The repository includes job_accounting.txt and the job output in logs/ as evidence.

3. Results and Interpretation

The simulation found that selling 111 tickets generated the highest average profit among the strategies tested, at $21,729.60 per flight.

Selling exactly 100 tickets produced an average profit of $20,000. Selling 111 tickets therefore increased simulated average profit by $1,729.60, or approximately 8.65%.

The results suggest that moderate overbooking can increase profitability because the additional ticket revenue outweighs the expected compensation costs. However, selling too many tickets eventually reduces average profit as more passengers need to be bumped.

This model is simplified. It assumes fixed ticket prices, independent no-show probabilities, and constant compensation costs. The results are estimates from a finite simulation rather than a guarantee that 111 tickets is always optimal.

4. AI Assistance and External Sources

I used ChatGPT (OpenAI) during this project to help plan the simulation, understand how to structure the Python functions and loops, and draft portions of the code. I also used it for guidance on testing, GitHub Actions, Mamba environment setup, and troubleshooting the SLURM job submission process.

I reviewed and modified the code during development rather than using the AI-generated suggestions without evaluation. I manually checked the profit calculations, tested different scenarios with pytest, verified that the fixed random seed produced consistent results, and ran the simulation on Great Lakes. I also inspected the SLURM output and accounting records to confirm that the job completed successfully.

AI was used as a coding and troubleshooting assistant. I was responsible for reviewing the implementation, making changes, testing the program, and verifying the final results.