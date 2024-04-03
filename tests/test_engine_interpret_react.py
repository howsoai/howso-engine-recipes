tb_filename = "engine_interpret_react.ipynb"


def test_predicted_mean_interval(tb):
    """
    Tested whether the mean of the generated values is within the
    prediction interval.
    """
    tb.inject(
        """
        global_residual = trainee.get_prediction_stats()['moid']['mae']
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
        global_residual = trainee.get_prediction_stats()['moid']['mae']
        r_val = react["action"].loc[0, 'moid']
        upper_limit = (r_val + global_residual)
        lower_limit = (r_val - global_residual)
        """
    )

    assert (tb.ref("action_value") <= tb.ref("upper_limit"))
    assert (tb.ref("action_value") >= tb.ref("lower_limit"))


def test_KDE_prediction_interval(tb):
    """
    Tested the percentage area under the curve for the KDE
    in relation to the prediction interval.
    """
    tb.inject(
        """
        from scipy.integrate import quad

        r_val = react["action"].loc[0, 'moid']
        global_residual = trainee.get_prediction_stats()['moid']['mae']
        lower_bound = r_val - global_residual
        upper_bound = r_val + global_residual

        from scipy.stats import gaussian_kde
        kde = gaussian_kde(gen_reacts)

        # Define the function to integrate (the KDE)
        def integrand(x):
            return kde(x)

        # Integrate and get area under the curve
        result, _ = quad(integrand, lower_bound, upper_bound)
        """
    )

    assert (tb.ref("result") >= tb.ref("0.45"))
