
# DataQualiPy

### A Lightweight Python Library for Dataset Quality Assessment and Profiling

DataQualiPy is an open-source Python library designed to help developers, data scientists, and machine learning practitioners assess dataset quality before performing data analysis or training machine learning models.

It provides an easy-to-use interface for inspecting datasets, identifying missing values, detecting duplicate records, and generating descriptive dataset profiles.

---

## Features

- **Dataset Loading:** Load datasets from CSV files or Pandas DataFrames.
- **Dataset Profiling:** Analyze dataset dimensions, column data types, missing values, unique values, and numerical statistics.
- **Missing Value Analysis:** Identify missing values in datasets.
- **Duplicate Detection:** Detect duplicate records.
- **Quality Score:** Calculate an initial heuristic dataset quality score.
- **Modular Architecture:** Designed to support additional validation and analysis features.

---

## Installation

Install DataQualiPy using pip:

```bash
pip install dataqualipy
```

**Note:** DataQualiPy is currently under active development. Some planned features may not yet be available.

---

## Quick Start

### 1. Import the library

```python
from dataqualipy import DataAudit
```

### 2. Load a CSV dataset

```python
audit = DataAudit("sample.csv")
```

You can also provide a Pandas DataFrame:

```python
import pandas as pd
from dataqualipy import DataAudit

df = pd.DataFrame({
    "name": ["Rahul", "Priya", "Amit"],
    "age": [21, 22, 20],
    "marks": [85, 90, 75]
})

audit = DataAudit(df)
```

### 3. Perform dataset quality analysis

```python
result = audit.run()

print(result)
```

Example output:

```python
{
    "rows": 3,
    "columns": 3,
    "missing_values": 0,
    "duplicates": 0,
    "quality_score": 100.0
}
```

### 4. Generate a dataset profile

```python
profile = audit.profile()

print(profile)
```

The profiler provides:
- Total number of rows and columns
- Column data types
- Missing-value counts
- Missing-value percentages
- Unique-value counts
- Numerical statistics such as mean, median, standard deviation, minimum, and maximum

---

## Project Structure

```text
DataQualiPy/
│
├── src/
│   └── dataqualipy/
│       ├── __init__.py
│       ├── core.py
│       ├── profiler.py
│       ├── validators.py
│       ├── detectors.py
│       ├── report.py
│       └── exceptions.py
│
├── tests/
│   ├── test_core.py
│   ├── test_profiler.py
│   └── test_integration.py
│
├── examples/
│   ├── basic_usage.py
│   └── sample.csv
│
├── README.md
├── LICENSE
├── .gitignore
└── pyproject.toml
```

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Dataset manipulation and analysis |
| NumPy | Numerical computing |
| Pytest | Unit and integration testing |
| Setuptools | Package building |
| PyPI | Python package distribution |

---

## Development Setup

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/DataQualiPy.git
```

Navigate to the project:

```bash
cd DataQualiPy
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install development dependencies:

```bash
python -m pip install -e ".[dev]"
```

Run tests:

```bash
python -m pytest -v
```

---

## Quality Score

DataQualiPy currently uses an initial heuristic quality score based on missing cells and duplicate rows.

The formula is:

\[
Q = \max(0, 100 \times (1 - M - D))
\]

Where:

- \(Q\) = Dataset quality score
- \(M\) = Ratio of missing cells to total cells
- \(D\) = Ratio of duplicate rows to total rows

**Disclaimer:** This is a preliminary heuristic, not a statistically validated measure of overall dataset quality. It does not currently account for incorrect values, inconsistent formats, or domain-specific validation rules.

---

## Testing

The project uses Pytest for automated testing.

Current verified tests cover:

- Dataset profiling
- DataAudit integration
- Basic dataset quality analysis

Run all tests:

```bash
python -m pytest -v
```

---

## Roadmap

- [x] CSV dataset loading
- [x] Pandas DataFrame support
- [x] Basic dataset quality analysis
- [x] Dataset profiling
- [x] Initial automated tests
- [x] DataAudit and profiler integration
- [ ] Missing-value validation
- [ ] Duplicate detection module
- [ ] Outlier detection using IQR and Z-score
- [ ] Schema and data-type validation
- [ ] Correlation analysis
- [ ] HTML and JSON report generation
- [ ] Comprehensive benchmarking
- [ ] PyPI release

---

## Contributing

Contributions, suggestions, and bug reports are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Add relevant tests.
5. Submit a Pull Request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

Built with Python and the open-source data science ecosystem.

**DataQualiPy — Making Dataset Quality Assessment Simpler.**
