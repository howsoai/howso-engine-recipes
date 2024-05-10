tb_filename = "sparse_data_validation.ipynb"


def test_accuracy_above_random(tb):
    """Ensure that 90% of the results are above the random choice line."""

    tb.inject(
        """
        acc_random_cmp = prediction_stats_df.accuracy > majority_class_accuracy
        assert acc_random_cmp.mean() >= 0.75
        """
    )
