
# Trigger-based experimental metadata embedding

This repository demonstrates a general approach for embedding experimental
metadata directly into recorded data streams using stimulus-derived trigger
signals.


- A stimulus channel acts as a trigger signal
- The same channel encodes metadata using pulse-duration modulation
- Metadata is represented as 8-bit binary values
- The encoded signal is recorded alongside experimental data

The example provided here uses visual stimulation monitored by a photodiode,
a common setup in visually driven neurophysiology experiments. Additional
stimulus modalities are possible.

This is how it looks when the signal is visualized:
![blogpost_1_a](https://github.com/user-attachments/assets/fa5a5f74-df6f-45d0-8e7b-ee590c445054)

![blogpost_1_b](https://github.com/user-attachments/assets/3e6fe8cb-83d0-402b-874f-352bcc8f08e5)

## Requirements
- Python
- PsychoPy


