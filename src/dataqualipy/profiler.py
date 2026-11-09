
import pandas as pd


class DatasetProfiler:

    def __init__(self, df):

        if not isinstance(df, pd.DataFrame):
            raise TypeError(
                "Input must be a Pandas DataFrame."
            )

        self.df = df.copy()

    def profile(self):

        rows, columns = self.df.shape

        column_profiles = {}

        for column in self.df.columns:

            series = self.df[column]

            missing_count = int(series.isnull().sum())

            missing_percentage = (
                (missing_count / rows) * 100
                if rows > 0 else 0.0
            )

            unique_count = int(series.nunique())

            column_info = {
                "data_type": str(series.dtype),
                "missing_values": missing_count,
                "missing_percentage": round(
                    missing_percentage, 2
                ),
                "unique_values": unique_count
            }

            if (
                pd.api.types.is_numeric_dtype(series)
                and not pd.api.types.is_bool_dtype(series)
            ):

                stats = series.describe()

                column_info["statistics"] = {
                    "mean": (
                        float(stats["mean"])
                        if pd.notna(stats["mean"]) else None
                    ),
                    "median": (
                        float(series.median())
                        if pd.notna(series.median()) else None
                    ),
                    "std": (
                        float(stats["std"])
                        if pd.notna(stats["std"]) else None
                    ),
                    "min": (
                        float(stats["min"])
                        if pd.notna(stats["min"]) else None
                    ),
                    "max": (
                        float(stats["max"])
                        if pd.notna(stats["max"]) else None
                    )
                }

            column_profiles[str(column)] = column_info

        return {
            "total_rows": rows,
            "total_columns": columns,
            "column_profiles": column_profiles
        }
