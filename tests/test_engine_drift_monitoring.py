tb_filename = "engine_drift_monitoring.ipynb"


def test_drift_agreement(tb):
    """
    Test that the howso and gradient boost models disagree with each other after the
    data drift

    """
    tb.inject(
        """
        before_drift = mismatch_count_rolling_df.iloc[:50].mean().iloc[0]
        after_drift = mismatch_count_rolling_df.iloc[50:].mean().iloc[0]
        """
    )

    assert tb.ref("after_drift") > tb.ref("before_drift")


def test_drift_KL(tb):
    """
    Test that the KL divergence is greater after the drift

    """
    assert tb.ref("kl_diff") > 0
