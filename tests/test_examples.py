from contextlib import redirect_stdout
import io


def test_example_engine():
    """Test the example_engine.py."""
    from example_engine import main

    f = io.StringIO()
    with redirect_stdout(f):
        accuracy = main()
    assert accuracy > 0.90


def test_example_scikit():
    """Test the example_scikit.py."""
    from example_scikit import main

    f = io.StringIO()
    with redirect_stdout(f):
        accuracy = main()
    assert accuracy > 0.90
