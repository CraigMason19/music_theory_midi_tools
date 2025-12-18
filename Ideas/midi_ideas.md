# project_outline.md

# Title
MIDI chord progression exporter
MIDI Chord Progressions

## Overview
- Brief summary of the project’s purpose
- What problem does it solve or explore?   
- Intended users or use-case


pyqt 6 interface and virtual env for midiutil and make a program that converts a text string
"V IV ii VI ......." as a chord midi in any key I want
Playback & Export – Play the MIDI live or save it for use in a DAW.
Real-time MIDI output – Send MIDI signals straight from your PyQt6 program into Reaper using a virtual MIDI port.



## Tech Stack
- Python (virtual env)
- Requires my music_theory package (from github)


## Rules
- Use typing


## MVP Features / Requirements



## Extras / Stretch Goals
- PyQt6 Interface
- Connect directly to reaper


## References / links







  




[General ideas]
```python
def Class MidiNote:
    def __init__(self, note: Note):
        self.note = note
        self.octave ?
        self.hertz ?


def Class Exporter:
    def __init__(self, prog: Progression):
        pass

    def export_sequence(self, tempo: number, num_repeitions: Number =1):
        pass

    


```
 






If i could send it to reaper live, I could type out any progression i want send it to reaper, put a piano vst on it loop it, and have instant backing tracks of any progression i like
Exactly! You’d be turning text input into real-time music, making Reaper an instant composition tool. Here’s how you could pull it off:

### **How to Send MIDI Live to Reaper**

1. **Use** `rtmidi` **or a Virtual MIDI Port**
    - Install `python-rtmidi` (`pip install python-rtmidi`).
    - Set up a virtual MIDI device (e.g., **LoopMIDI** or Reaper’s built-in MIDI input).
    - Python sends MIDI messages directly to Reaper.
    - 
2. **Generate MIDI Events Dynamically**
    - Convert `"V IV ii VI"` into MIDI notes in the selected key.
    - Send note-on/note-off events continuously.
    - Set tempo and timing (e.g., chord changes every measure).
    - 
3. **Process MIDI Inside Reaper**
    - Assign the incoming MIDI to a **piano VST**.
    - Loop the progression in a MIDI track.
    - Tweak timing, quantization, and effects.



Example: Sending MIDI from Python
python
import rtmidi
import time

midiout = rtmidi.MidiOut()
midiout.open_virtual_port("Python MIDI")

chords = [[60, 64, 67], [62, 65, 69], [57, 60, 64], [59, 62, 66]]  # Example chord notes

for chord in chords:
    for note in chord:
        midiout.send_message([0x90, note, 100])  # Note on
    time.sleep(1)  # Hold for 1 second
    for note in chord:
        midiout.send_message([0x80, note, 100])  # Note off

midiout.close_port()
Now, instead of manually programming MIDI tracks in Reaper, you could type out a progression, hit send, and instantly loop it with a piano VST! You’d have on-demand backing tracks for composition, improvisation, or theory testing.

Would this fit your workflow? You’d basically be coding your own instant jam session