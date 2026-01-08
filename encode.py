"""
Photodiode-based encoding of experimental metadata using pulse-duration modulation.

This script demonstrates how to embed experiment metadata into a recorded
photodiode channel by encoding characters as sequences of light pulses
with different durations.
"""

from psychopy import visual, core
import random


# =========================
# Window setup
# =========================

win = visual.Window(
    size=[1920, 1080],
    color="#FFFFFF",
    fullscr=True,
    monitor="LG",
    screen=1,
    waitBlanking=False,
)


# =========================
# Background
# =========================

background = visual.Rect(
    win,
    size=(10, 10),
    fillColor="#FFFFFF",
    pos=(0, 0),
)


# =========================
# Photodiode square setup
# =========================

DIODE_SIZE = (0.3, 0.3)
DIODE_POSITION = (0.9, -0.9)

diode_off = visual.Rect(
    win,
    size=DIODE_SIZE,
    pos=DIODE_POSITION,
    fillColor="#000000",
    lineColor="#000000",
)

diode_on = visual.Rect(
    win,
    size=DIODE_SIZE,
    pos=DIODE_POSITION,
    fillColor="#FFFFFF",
    lineColor="#FFFFFF",
)


# =========================
# Experimental metadata
# =========================

experiment_id = "D"

stimuli_pairs = [
    ("stim_a", "stim_b"),
    ("stim_c", "stim_d"),
    ("stim_e", "stim_f"),
]

order = list(range(len(stimuli_pairs)))
random.shuffle(order)
order_string = "".join(str(i) for i in order)


# =========================
# Encoding function
# =========================

def encode_word_via_diode(
    word,
    win,
    square_off,
    square_on,
    short_duration=0.02,
    long_duration=0.08,
    gap_duration=0.1,
):
    """
    Encode a string as a sequence of photodiode light pulses.

    Encoding scheme:
        - Each character is converted to 8-bit ASCII.
        - Bit '0'  -> short pulse
        - Bit '1'  -> long pulse
        - OFF state is represented by square_off.
        - Start and stop markers are long pulses.

    Parameters
    ----------
    word : str
        String to encode.
    win : psychopy.visual.Window
        PsychoPy window object.
    square_off : psychopy.visual.Rect
        Photodiode square in OFF state.
    square_on : psychopy.visual.Rect
        Photodiode square in ON state.
    short_duration : float
        Duration (s) of short pulse.
    long_duration : float
        Duration (s) of long pulse.
    gap_duration : float
        Inter-pulse gap duration (s).
    """

    # Start marker
    square_on.draw()
    win.flip()
    core.wait(long_duration)

    square_off.draw()
    win.flip()
    core.wait(gap_duration)

    for char in word:
        binary_str = format(ord(char), "08b")
        for bit in binary_str:
            square_on.draw()
            win.flip()
            core.wait(short_duration if bit == "0" else long_duration)

            square_off.draw()
            win.flip()
            core.wait(gap_duration)

    # Stop marker
    square_on.draw()
    win.flip()
    core.wait(long_duration)

    square_off.draw()
    win.flip()


# =========================
# Run encoding
# =========================

background.draw()
diode_off.draw()
win.flip()
core.wait(2)

encode_word_via_diode(experiment_id, win, diode_off, diode_on)
core.wait(1)

encode_word_via_diode(order_string, win, diode_off, diode_on)

diode_off.draw()
win.flip()
core.wait(5)

win.close()
core.quit()






