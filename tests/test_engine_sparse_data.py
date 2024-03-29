tb_filename = "engine_sparse_data.ipynb"


def test_accuracy_above_random(tb):
    """Ensure that 90% of the results are above the random choice line."""

    tb.inject(
        """
        acc_random_cmp = prediction_stats_df.accuracy > random_value
        assert acc_random_cmp.mean() >= 0.75
        """
    )
