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

## PW2 --- Lab B: Optimization in Chemistry

Part 2: Method Comparison
- Convex f(x): GD, Newton, and SLSQP all converged to x = 3.0000.
- Non-Convex g(x):
  - x0 = 0.0: GD & SLSQP found global min (x ≈ -1.3009); Newton hit local max (x ≈ 0.1699).
  - x0 = 2.0: GD & Newton hit local min (x ≈ 1.1309); SLSQP found global min (x ≈ -1.3006).

Part 3: Reaction Rate Fitting
- Fitted k ≈ 0.2618 s^-1 (Saved: PW2/Lab B/kinetics.png).

Part 4: Chemical Equilibrium
- x ≈ 0.6638 mol (nH2 = nI2 ≈ 0.3362 mol, nHI ≈ 1.3277 mol).
- Both Newton and SLSQP yielded identical results (Saved: PW2/Lab B/equilibrium.png).

Part 5: Titration Equivalence Point
- Equivalence point: V_eq = 50.0 mL (Saved: PW2/Lab B/titration.png).