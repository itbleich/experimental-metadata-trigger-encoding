# In-recording embedding of experimental metadata
This repository presents a simple method for embedding experiment log information directly into a neurophysiology recording channel, ensuring that metadata and neural data remain tightly linked.

This approach uses a stimulus channel that functions as a trigger signal and additionally leverages that signal to embed experimental metadata directly within the recorded data stream. Metadata is represented in binary form, with characters encoded as 8-bit values, and pulse duration serves as the encoding marker. In the implementation shown here, the stimulus channel relies on visual stimulation monitored by a photodiode, a common approach in visually driven experiments, though alternative stimulus modalities are also possible.

## Encoding scheme

-Two display states are used: square_0, a black square corresponding to no photodiode stimulation, and square_1, a white square corresponding to maximal photodiode stimulation. These states can also be used during the experiment as general on/off trigger markers.

-Bit 0 is encoded as a short ON pulse.

-Bit 1 is encoded as a long ON pulse.

-OFF gaps separate consecutive pulses.

-Characters are encoded using 8-bit ASCII representation.

-Long ON pulses at the beginning and end of each message serve as start and stop markers.


