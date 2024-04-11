tb_filename = "engine_timeseries.ipynb"


def test_r2(tb):
    """Ensure good r2 given the dataset."""

    tb.inject(
        """
        r2 = results['f1']['r2']
        """
    )

    assert tb.ref("r2") >= 0.9


def test_check_synth(tb):
    """Ensure enough data is synthesized."""
    tb.inject(
        """
        passing = True
        for series_id in result_gen["ID"].unique():
            series_df = result_gen.loc[result_gen['ID'] == series_id]
            if len(series_df) < 100:
                passing = False
        """
    )

    assert tb.ref("passing")
