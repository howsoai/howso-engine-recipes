tb_filename = "advanced_features/engine_json_features.ipynb"


def test_action_length(tb):
    """Ensure good accuracy given the dataset."""

    tb.inject(
        """
        assert len(discriminative_action) == 1
        assert len(generative_reaction_25) == 5
        assert len(generative_reaction_1) == 5
        """
    )
