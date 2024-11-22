import numpy as np

tb_filename = "interpret_react.ipynb"


def test_predicted_mean_interval(tb):
    """
    Test whether the mean of the generated values is within the
    prediction interval.
    """
    tb.inject(
        """
        global_residual = trainee.get_prediction_stats(details={"prediction_stats":True})['moid']['mae']
        r_val = react["action"].loc[0, 'moid']
        upper_limit = (r_val + global_residual)
        lower_limit = (r_val - global_residual)

        mean_gen_react = sum(gen_reacts) / len(gen_reacts)
        """
    )

    assert (tb.ref("mean_gen_react") <= tb.ref("upper_limit"))
    assert (tb.ref("mean_gen_react") >= tb.ref("lower_limit"))


def test_boundary_values(tb):
    """
    Test if the boundary values were computed correctly.
    """
    boundary_values = tb.ref("boundary_values")

    assert boundary_values['e'][0] is None  # no boundary below the value for e
    assert 0.19 <= boundary_values['e'][1] <= 0.26

    assert 1.65 <= boundary_values['q'][0] <= 1.89
    assert boundary_values['q'][1] is None  # no boundary above the value for q
