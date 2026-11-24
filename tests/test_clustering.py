tb_filename = "clustering.ipynb"


def test_clustering_accuracy(tb):
    """Ensure good accuracy for test data."""
    assert tb.ref("adjusted_rand_index") > 0.8
