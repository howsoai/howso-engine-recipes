tb_filename = "3-anomaly_detection.ipynb"


def test_outliers(tb):
    """Ensure outliers are detected."""
    assert tb.ref("outliers").shape[0] > 0


def test_inliers(tb):
    """Ensure inliers are detected."""
    assert tb.ref("inliers").shape[0] > 0
