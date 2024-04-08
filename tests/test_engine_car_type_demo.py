tb_filename = "engine_car_type_demo.ipynb"
tb_dir = "inference"


def test_car_type_accuracy(tb):
    """Ensure good accuracy for test data."""
    assert float(tb.ref("accuracy")) > 0.90
