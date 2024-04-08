tb_filename = "engine_clustering.ipynb"
tb_dir = "clustering"


def test_clustering_accuracy(tb):
    """Ensure good accuracy for test data."""
    assert tb.ref("dist_contribution_acc") > 0.8
