import numpy as np

tb_filename = "fuzzy_matching.ipynb"


def test_accuracy(tb):
    """Ensure decent accuracy."""
    assert np.mean(tb.ref("acc")) >= 0.5
