tb_filename = "1-engine-intro.ipynb"


def test_accuracy(tb):
    """Ensure good accuracy given the dataset."""

    tb.inject(
        """
        accuracy = stats["accuracy"]
        """
    )

    assert float(tb.ref("accuracy")) >= 0.7


def test_conditional_accuracies(tb):
    """Ensure overall accuracy lies between accuracy of each sex"""

    sex_0_accuracy = tb.ref('sex_0_stats["accuracy"]')
    sex_1_accuracy = tb.ref('sex_1_stats["accuracy"]')
    overall_accuracy = tb.ref('stats["accuracy"]')

    assert sex_0_accuracy > 0.65
    assert sex_1_accuracy > 0.65

    if overall_accuracy < sex_1_accuracy and overall_accuracy < sex_0_accuracy:
        # smaller than both
        assert False
    elif overall_accuracy > sex_1_accuracy and overall_accuracy > sex_0_accuracy:
        # greater than both
        assert False
