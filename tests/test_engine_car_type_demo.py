tb_filename = "engine_car_type_demo.ipynb"


def test_1_engine_accuracy(tb):
    """Ensure good accuracy for test data."""
    assert tb.ref("accuracy_score") > 0.90
