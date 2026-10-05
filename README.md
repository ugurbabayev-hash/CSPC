# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup

Create the environment for a given lab:

conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**
- Set up the CSPC repository structure, Conda environment, Git version control, unit tests with pytest, and a NumPy speed benchmark.

**Speed comparison (loop vs NumPy):**
- loop : 1.8702 s
- numpy : 0.0002 s
- speed-up: 11548.36 x faster

**Tests:** all passing? yes

**Conclusion:**
- NumPy code is much faster than standard Python loops for simulations.
- Automated tests with pytest help verify that the code works correctly without manual checks.
- Setting up Conda and Git makes the project clean, reliable, and easy to run anywhere.

## PW1 --- Lab B

- **Data Findings:** The dataset records radioactive counts dropping exponentially over time.
- **Analytical Match:** The scatter plot of observed data matches the smooth analytical decay curve ($N_0 e^{-\lambda t}$) closely across the entire time range.
- **Snakemake Pipeline:** The Snakemake workflow tracks file dependencies (`decay_observed.csv` and `plot.py`) to automatically rebuild `figure.png` whenever inputs change, preventing unnecessary recalculations.

## PW2 - Lab A: Motion from Tracking Data

- **Measured Mean Acceleration:** ~ -8.58 m/s² (close to Earth's gravity).
- **The Noise Problem:** Taking the derivative of position data amplifies tiny measurement errors. Even though the position curve looks smooth, the calculated acceleration swings wildly (std dev: 28.72).
- **Integration Result:** Integrating the noisy acceleration back up suppresses the noise. The recovered position matches the original data almost perfectly (max difference: ~0.78 m).
- **Bonus (2D Trajectory):** Successfully tracked 2D movement from `trajectory.csv`, calculated velocity for both $x$ and $y$ coordinates, and plotted the overall speed over time.