tb_filename = "audit_edit.ipynb"


def test_accuracy_comparison(tb):
    """Ensure edited accuracy is higher than original accuracy."""
    assert tb.ref("accuracy_new") > tb.ref("accuracy")


def test_accuracy(tb):
    """Ensure new accuracy is above threshold."""
    assert tb.ref("accuracy_new") >= 0.75
