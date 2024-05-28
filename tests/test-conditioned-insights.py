tb_filename = "conditioned-insights.ipynb"


def test_final_output(tb):
    """
    Test that sex_1_conditioned_accuracy is not 0.
    """

    assert len(tb.ref("sex_1_conditioned_accuracy")) > 0
