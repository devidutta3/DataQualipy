
import pandas as pd
from pathlib import Path

from .profiler import DatasetProfiler


class DataAudit:
    """
    Main interface for dataset quality analysis.

    Supports CSV files and Pandas DataFrames.
    """

    def __init__(self, data):
        """
        Initialize DataAudit with a CSV file
        or Pandas DataFrame.
        """
        self.data = data
        self.df = self._load_data()

    def _load_data(self):
        """
        Load dataset from CSV or DataFrame.
        """

        if isinstance(self.data, pd.DataFrame):
            return self.data.copy()

        path = Path(self.data)

        if not path.exists():
            raise FileNotFoundError(
                f"Dataset not found: {path}"
            )

        if path.suffix.lower() == ".csv":
            return pd.read_csv(path)

        raise ValueError(
            "Currently only CSV files are supported."
        )

    def run(self):
        """
        Perform basic dataset quality analysis.

        Returns:
            dict: Basic dataset quality metrics.
        """

        rows, columns = self.df.shape

        missing = int(
            self.df.isnull().sum().sum()
        )

        duplicates = int(
            self.df.duplicated().sum()
        )

        total_cells = rows * columns

        if total_cells == 0:
            quality_score = 0.0

        else:
            missing_ratio = missing / total_cells

            duplicate_ratio = (
                duplicates / rows if rows else 0
            )

            quality_score = max(
                0.0,
                100 * (
                    1 - missing_ratio - duplicate_ratio
                )
            )

        return {
            "rows": rows,
            "columns": columns,
            "missing_values": missing,
            "duplicates": duplicates,
            "quality_score": round(
                quality_score, 2
            )
        }

    def profile(self):
        """
        Generate detailed dataset profiling.

        Returns:
            dict: Dataset and column-level statistics.
        """

        profiler = DatasetProfiler(self.df)

        return profiler.profile()
