tb_filename = "ablation_demo.ipynb"


def test_ablated_size(tb):
    """Test that auto-ablation reduced the number of trained cases."""
    assert tb.ref("num_trained_cases") < tb.ref("num_total_cases")
    assert tb.ref("num_trained_percent") < 50
