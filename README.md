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
- Vectorised computations in NumPy run significantly faster than pure-Python loops for large simulations. Automated pytest tests guarantee code reliability and proper error handling. Setting up Git and Conda provides a solid, reproducible workflow for practical projects.