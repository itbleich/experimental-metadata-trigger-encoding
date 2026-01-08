# In-recording embedding of experimental metadata
This repository presents a simple method for embedding experiment log information directly into a neurophysiology recording channel, ensuring that metadata and neural data remain tightly linked.

This approach uses a stimulus channel that functions as a trigger signal and additionally leverages that signal to embed experimental metadata directly within the recorded data stream. Metadata is represented in binary form, with characters encoded as 8-bit values, and pulse duration serves as the encoding marker. In the implementation shown here, the stimulus channel relies on visual stimulation monitored by a photodiode, a common approach in visually driven experiments, though alternative stimulus modalities are also possible.

# Trigger-based experimental metadata embedding

This repository demonstrates a general approach for embedding experimental
metadata directly into recorded data streams using stimulus-derived trigger
signals.

## Overview
- A stimulus channel acts as a trigger signal
- The same channel encodes metadata using pulse-duration modulation
- Metadata is represented as 8-bit binary values
- The encoded signal is recorded alongside experimental data

## Implementation
The example provided here uses visual stimulation monitored by a photodiode,
a common setup in visually driven neurophysiology experiments. Additional
stimulus modalities are possible. 

## Requirements
- Python
- PsychoPy


