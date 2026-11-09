
import pandas as pd
import pytest

from dataqualipy.profiler import DatasetProfiler


def test_dataset_profile():

    df = pd.DataFrame({
        "name": ["Rahul", "Priya", "Amit"],
        "age": [21, 22, 20],
        "marks": [85, 90, 75]
    })

    profiler = DatasetProfiler(df)
    result = profiler.profile()

    assert result["total_rows"] == 3
    assert result["total_columns"] == 3

    assert result["column_profiles"]["age"]["unique_values"] == 3

    assert result["column_profiles"]["marks"]["statistics"]["mean"] == pytest.approx(83.33333333333333)