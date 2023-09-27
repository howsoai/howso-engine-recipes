tb_filename = "engine_predict_explain_show.ipynb"


def test_accuracy(tb):
    """Ensure sufficient accuracy for data set."""
    assert tb.ref("accuracy") >= 0.65


def test_outliers(tb):
    """Ensure outliers are detected."""
    assert tb.ref("outliers").shape[0] > 0


def test_inliers(tb):
    """Ensure inliers are detected."""
    assert tb.ref("inliers").shape[0] > 0


def test_potential_improvements(tb):
    """Ensure the improvement dataframes exist."""
    assert tb.ref("partial_train_df").shape[0] > 0
