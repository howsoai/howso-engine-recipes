tb_filename = "conditioned-insights.ipynb"


def test_conditioned_accuracy(tb):
    """Test that both conditioned accuracies are computed and are valid proportions."""
    for name in ("male_conditioned_accuracy", "female_conditioned_accuracy"):
        assert 0 < float(tb.ref(name)) <= 1
