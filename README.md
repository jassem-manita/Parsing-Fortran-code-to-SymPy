# Parsing Fortran Code to SymPy - Experiments

Experimental repository for testing the LFortran → SymPy conversion pipeline.

## Setup Note

**Issue encountered**: Couldn't reliably import lfortran as a Python module due to conda/python environment conflicts.

**Solution**: I used lfortran directly via its full path. This works reliably for now.

## Installation

1. Install LFortran (using conda):
```bash
   conda create -n lfortran lfortran -c conda-forge
```

2. **Configure path**:

   
   Add and Edit `config.py` and set your LFortran path:
```python
   LFORTRAN_PATH = "/path/to/miniconda3/envs/lfortran/bin/lfortran"
```
   
   Find your path with: `which lfortran` (after activating conda env)

3. **Install Python dependencies**:
```bash
   pip install -r requirements.txt
```

## Usage
```bash
python inspect_asr.py
```

This will parse `01_simple.f90` file and show their ASR (Abstract Semantic Representation).

## Project Structure
```
.
├── fortran_samples/        # Fortran test files (.f90)
├── inspect_asr.py          # Main script to extract ASR
├── config.py               # LFortran path (git-ignored)
└── README.md
```