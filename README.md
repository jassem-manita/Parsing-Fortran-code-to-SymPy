
# Parsing Fortran Code to SymPy

This project demonstrates parsing Fortran code using LFortran and converting expressions to SymPy.

## Installation

1. Install LFortran (conda-forge only):
   - See: https://docs.lfortran.org/
   - Example:
     ```bash
     conda create -n lfortran lfortran -c conda-forge
     ```
2. Set your LFortran path in `config.py`:
   ```python
   LFORTRAN_PATH = "/path/to/lfortran"
   ```
3. Install Python dependencies:
   - With pip:
     ```bash
     pip install -r requirements.txt
     ```
   - Or with conda:
     ```bash
     conda install sympy pytest -c conda-forge
     ```

## Usage

Inspect ASR:
```bash
python inspect_asr.py
```

Convert ASR to SymPy:
```bash
python extract_to_sympy.py
```
