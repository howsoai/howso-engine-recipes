tb_filename = "bias_mitigation.ipynb"


def test_accuracy(tb):
    """
    Test that the final distribution is significantly less biased
    """

    assert tb.ref("decrease_fold") > 2
