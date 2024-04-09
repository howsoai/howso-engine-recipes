tb_filename = "car_type_demo.ipynb"


def test_car_type_accuracy(tb):
    """Ensure good accuracy for test data."""
    assert float(tb.ref("accuracy")) > 0.90
