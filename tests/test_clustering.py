tb_filename = "clustering.ipynb"


def test_clustering_accuracy(tb):
    """Ensure good accuracy for test data."""
    assert tb.ref("dist_contribution_acc") > 0.8
