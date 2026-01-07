# In-recording embedding of experimental metadata
This repository presents a simple method for embedding experiment log information directly into a neurophysiology recording channel, ensuring that metadata and neural data remain tightly linked.

This approach uses a stimulus channel that is transduced into a recorded signal and employed to embed experimental metadata directly within the data stream. Metadata is represented in binary form, with characters encoded as 8-bit values. Pulse duration is used as the encoding marker. The stimulus channel used here relies on visual stimulation monitored by a photodiode, a common method in experiments with visual stimulation, though alternative approaches are also possible.

## Encoding scheme

- Bit `0` → short ON pulse  
- Bit `1` → long ON pulse  
- OFF gaps separate pulses  
- Characters are encoded as 8-bit ASCII  
- Long pulses at the beginning and end serve as start/stop markers  


