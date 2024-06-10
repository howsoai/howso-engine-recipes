tb_filename = "model_monitoring.ipynb"


def test_drift_monitoring(tb):
    """
    Test that the recipe runs until the last conviction metric and that all the convictions come back.
    """
    tb.inject(
        """
        len_convictions = len(avg_convictions)
        """
    )

    assert tb.ref("len_convictions") == 14
