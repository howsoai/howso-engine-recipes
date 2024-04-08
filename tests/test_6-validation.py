tb_filename = "6-validation.ipynb"
tb_dir = "getting_started"


def test_final_output(tb):
    """
    Test that the final_output outputs actual values.
    """

    assert len(tb.ref("final_output")) > 0
