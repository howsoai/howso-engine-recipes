tb_filename = "predict_explain_show.ipynb"


def test_accuracy(tb):
    """Ensure sufficient accuracy for data set."""
    tb.inject("assert accuracy >= 0.65")


def test_outliers(tb):
    """Ensure outliers are detected."""
    tb.inject("assert outliers.shape[0] > 0")


def test_inliers(tb):
    """Ensure inliers are detected."""
    tb.inject("assert inliers.shape[0] > 0")


def test_potential_improvements(tb):
    """Ensure the improvement dataframes exist."""
    tb.inject("assert partial_train_df.shape[0] > 0")
