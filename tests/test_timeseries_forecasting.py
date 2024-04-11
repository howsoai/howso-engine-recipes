tb_filename = "timeseries_forecasting.ipynb"


def test_forecasting(tb):
    """Ensure forecasts aren't too long."""

    tb.inject(
        """
        max_forecast_time = synth_df['time'].max().item()
        """
    )
    assert tb.ref("max_forecast_time") < 4.5
