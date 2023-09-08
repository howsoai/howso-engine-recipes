tb_filename = "5-bias_mitigation.ipynb"

def test_accuracy(tb):
    """
    Test that the final distribution is correct.
    """

    assert tb.ref("p_value") < 0.1
