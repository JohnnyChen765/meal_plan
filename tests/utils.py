import pandas as pd


def assert_df_are_equal(df1: pd.DataFrame, df2: pd.DataFrame) -> None:
    pd.testing.assert_frame_equal(df1, df2)
    # assert df1.to_dict() == df2.to_dict()


def assert_series_are_equal(df1: pd.Series, df2: pd.Series) -> None:
    pd.testing.assert_series_equal(df1, df2)
