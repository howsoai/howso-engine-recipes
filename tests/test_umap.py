tb_filename = "umap.ipynb"


def test_completed(tb):
    assert tb.ref("min_dist") > 0
    assert tb.ref("k") is not None
