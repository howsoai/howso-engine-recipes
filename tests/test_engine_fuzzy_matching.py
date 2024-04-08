import numpy as np

tb_filename = "engine_fuzzy_matching.ipynb"
tb_dir = "time_series"


def test_accuracy(tb):
    """Ensure decent accuracy."""
    assert np.mean(tb.ref("acc")) >= 0.5
