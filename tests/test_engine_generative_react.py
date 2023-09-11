tb_filename = "engine_generative_react.ipynb"


def test_gen_highconv_acc(tb):
    """Ensure good accuracy given the dataset discriminative react."""

    tb.inject(
        """
        accuracy = acc_disc
        """
    )

    assert tb.ref("accuracy") >= 0.5

def test_compare_gen_conv_acc(tb):
    """Ensure that higher conviction generative react has a higher accuracy than the lower conviction generative react."""

    tb.inject(
        """
        accuracy_high = acc_gen_high
        accuracy_low = acc_gen_low
        """
    )

    assert tb.ref("accuracy_high") >= tb.ref("accuracy_low")


def test_synth_length(tb):
    """Ensure synthetic dataset lenght equals the desired length"""

    desired_len = tb.ref('len(df)')
    synth_len = tb.ref('len(synthetic_data)')

    assert desired_len == synth_len
