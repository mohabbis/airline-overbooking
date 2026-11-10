# Airline Overbooking Simulation


## Project Overview

This project uses a Python simulation to determine how many tickets an airline should sell for a flight with 100 seats to maximize its expected profit.

Airlines sometimes overbook flights because not every passenger shows up. Selling additional tickets increases revenue, but if too many passengers arrive, the airline must pay compensation.

My simulation assumes 100 seats, $200 per ticket, a 10% no-show probability, and $400 in compensation per bumped passenger. It tests selling between 100 and 120 tickets, simulating 1,000 flights for each quantity. I used a random seed of 42 to make the results reproducible.

## Running the Project

The project uses Python 3.11 and Mamba.

To create and activate the environment:

`mamba env create -f environment.yml`

`mamba activate airline-overbooking`

To run the simulation:

`python simulation.py`

To run the tests:

`python -m pytest -v`

All seven tests passed.

To run the simulation on Great Lakes, first create the environment at the path expected by the SLURM script:

`module load mamba/py3.11`

`mamba env create -f environment.yml --prefix ~/.conda/envs/airline-overbooking`

Then submit the job:

`mkdir -p logs`

`sbatch run.slurm`

The SLURM script uses the COMPFOR 203 course allocation. My job (65869603) completed successfully on compute node gl3025 with an exit code of 0:0. The output is saved in the logs folder, and the job accounting information is in job_accounting.txt.

## Results

The highest average profit was $21,729.60 when selling 111 tickets.

Selling only 100 tickets generated $20,000 in profit, so overbooking by 11 tickets increased simulated average profit by $1,729.60, or approximately 8.65%.

The results show that moderate overbooking can increase profit, but selling too many tickets increases compensation costs. The model uses simplified assumptions, so 111 tickets is the best result from this simulation rather than a guaranteed optimal strategy.

## AI Assistance

I used ChatGPT (OpenAI, November 10, 2026) to help plan the simulation, structure Python functions and loops, and draft portions of the code. I also used it for assistance with testing, GitHub Actions, Mamba, and troubleshooting SLURM on Great Lakes.

I reviewed and modified the code during development, manually verified the profit calculations, tested different scenarios using pytest, and checked that the results were reproducible. I also submitted the job to Great Lakes and verified its successful execution.

AI assisted with coding and troubleshooting, but I was responsible for reviewing, modifying, testing, and validating the program.
