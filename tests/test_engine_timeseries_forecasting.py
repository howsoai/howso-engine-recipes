tb_filename = "engine_timeseries_forecasting.ipynb"


def test_forecasting(tb):
    """Ensure forecasts don't end too early and aren't too long."""

    tb.inject(
        """
        forecast_lengths = synth_df.groupby('id').size()
        last_forecast_ys = synth_df.sort_values('time', ascending=False).drop_duplicates('id')['y']
        """
    )

    assert tb.ref("last_forecast_ys").max() < 40
    assert tb.ref("forecast_lengths").max() < 50
