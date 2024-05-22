tb_filename = "conditioned-insights.ipynb"


def test_final_output(tb):
    """
    Test that category is not empty.
    """

    assert len(tb.ref("category")) > 0
