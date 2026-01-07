# In-recording embedding of experimental metadata
Keeping accurate experiment logs is both essential and fragile. During data collection, experimental details often feel obvious and well documented, yet weeks or months later—when analysis begins—critical information may turn out to be missing, ambiguous, or difficult to align with the recorded data.

This repository presents a simple method for embedding experiment log information **directly into a neurophysiology recording channel**, ensuring that metadata and neural data remain tightly linked in time and structure.

This approach uses a stimulus channel (e.g., visual, auditory, or other) that is transduced into a recorded signal and employed to embed experimental metadata directly within the data stream. Metadata is represented in binary form, with characters encoded as 8-bit values.Information is conveyed through the temporal structure of the signal using pulse duration as the encoding marker, enabling reliable reconstruction of the original metadata from the recorded signal during offline analysis.

---

## Concept

- A small square on the stimulus display is dedicated to photodiode signaling.
- A photodiode placed over this square is recorded as an analog channel.
- Metadata (e.g. condition labels, trial identifiers) is encoded as a sequence of light pulses.
- Information is encoded **only in pulse duration**, not brightness.

This design is:
- robust to luminance calibration differences
- easy to threshold and decode offline
- compatible with standard electrophysiology setups

---

## Encoding scheme

- Bit `0` → short ON pulse  
- Bit `1` → long ON pulse  
- OFF gaps separate pulses  
- Characters are encoded as 8-bit ASCII  
- Long pulses at the beginning and end serve as start/stop markers  

All pulses use the same brightness level.

---
