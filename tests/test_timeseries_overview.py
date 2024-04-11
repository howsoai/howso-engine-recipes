tb_filename = "timeseries_overview.ipynb"


def test_r2(tb):
    """Ensure good r2 given the dataset."""

    tb.inject(
        """
        r2 = results['f1']['r2']
        """
    )

    assert tb.ref("r2") >= 0.9
