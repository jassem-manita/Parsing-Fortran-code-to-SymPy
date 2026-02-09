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
├── inspect_asr.py          # ASR inspection script
├──extract_to_sympy.py     # ASR to SymPy conversion
├── config.py               # LFortran path (git-ignored)
└── README.md
```

## Experiments

### Experiment 01: Basic ASR Inspection
Parse simple Fortran and examine ASR structure.
```bash
python inspect_asr.py
```

### Experiment 02: ASR to SymPy Conversion

Extract expressions from ASR and convert to SymPy.

**Input**: `y = 2.0 * x + 3.0`  
**Output**: SymPy expression `2.0*x + 3.0`
```bash
python extract_to_sympy.py
```

**Issues Faced & Solutions**:

1. **ANSI Color Codes in ASR Output**
   - Problem: LFortran outputs ASR with ANSI color codes (`\x1b[35m`, etc...) that broke regex patterns
   - Solution: Strip color codes before parsing: `re.sub(r'\x1b\[[0-9;]*m', '', asr)`

2. **Whitespace**
   - Problem: ASR indentation prevented regex matching
   - Solution: Strip each line before pattern matching

**Current Limitations**:
- Expression building is hardcoded for this pattern `c1 * x + c2`
