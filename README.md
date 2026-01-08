
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


