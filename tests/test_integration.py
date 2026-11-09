
import pandas as pd

from dataqualipy import DataAudit


def test_dataaudit_integration():

    df = pd.DataFrame({
        "name": ["Rahul", "Priya", "Amit"],
        "age": [21, 22, 20],
        "marks": [85, 90, 75]
    })

    audit = DataAudit(df)

    # Test basic quality analysis
    result = audit.run()

    assert result["rows"] == 3
    assert result["columns"] == 3
    assert result["missing_values"] == 0

    # Test detailed profiling
    profile = audit.profile()

    assert profile["total_rows"] == 3
    assert profile["total_columns"] == 3

    assert (
        profile["column_profiles"]["age"]["unique_values"]
        == 3
    )
