tb_filename = "feature_importance.ipynb"


def test_accuracy(tb):
    """Ensure that the notebook runs and runs a comparison dataframe."""

    assert len(tb.ref("comparison")) > 0
