tb_filename = "drift_monitoring.ipynb"


def test_drift_agreement(tb):
    """
    Test that the howso and gradient boost models disagree with each other after the
    data drift

    """
    tb.inject(
        """
        mismatch_count_rolling_df = mismatch_count_df.rolling(5).mean()
        before_drift = mismatch_count_rolling_df.iloc[:50].mean().iloc[0]
        after_drift = mismatch_count_rolling_df.iloc[50:].mean().iloc[0]
        """
    )

    assert tb.ref("after_drift") > tb.ref("before_drift")
