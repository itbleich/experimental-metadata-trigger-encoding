from psychopy import core


def encode_word_via_diode(
    word,
    win,
    square_0,
    square_1,
    short_duration=0.02,
    long_duration=0.08,
    gap_duration=0.1,
):
    """
    Encode a word using pulse-duration modulation.

    Bit encoding:
      - '0' -> short pulse
      - '1' -> long pulse

    All pulses use the same brightness (square_1).
    OFF state is square_0.
    """

    # Start marker: long pulse
    square_1.draw()
    win.flip()
    core.wait(long_duration)

    square_0.draw()
    win.flip()
    core.wait(gap_duration)

    for char in word:
        binary_str = format(ord(char), "08b")
        for bit in binary_str:
            square_1.draw()
            win.flip()
            core.wait(short_duration if bit == "0" else long_duration)

            square_0.draw()
            win.flip()
            core.wait(gap_duration)

    # Stop marker: long pulse
    square_1.draw()
    win.flip()
    core.wait(long_duration)

    square_0.draw()
    win.flip()
