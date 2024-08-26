tb_filename = "interpret_react.ipynb"


def test_predicted_mean_interval(tb):
    """
    Tested whether the mean of the generated values is within the
    prediction interval.
    """
    tb.inject(
        """
        global_residual = trainee.react_aggregate(details={"feature_residuals_robust": True})["moid"].iloc[0]
        r_val = react["action"].loc[0, 'moid']
        upper_limit = (r_val + global_residual)
        lower_limit = (r_val - global_residual)

        mean_gen_react = sum(gen_reacts) / len(gen_reacts)
        """
    )

    assert (tb.ref("mean_gen_react") <= tb.ref("upper_limit"))
    assert (tb.ref("mean_gen_react") >= tb.ref("lower_limit"))


def test_predicted_value_interval(tb):
    """
    Tested whether the actual value is within the prediction interval.
    """
    tb.inject(
        """
        global_residual = trainee.react_aggregate(details={"feature_residuals_robust": True})["moid"].iloc[0]
        r_val = react["action"].loc[0, 'moid']
        upper_limit = (r_val + global_residual)
        lower_limit = (r_val - global_residual)
        """
    )

    assert (tb.ref("action_value") <= tb.ref("upper_limit"))
    assert (tb.ref("action_value") >= tb.ref("lower_limit"))
