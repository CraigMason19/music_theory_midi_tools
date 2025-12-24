import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from music_theory import Note
from music_theory_midi_tools.midi_note import MIDINote


 

 





mn = MIDINote(Note.C, 4)


print(str(mn))
print(repr(mn))
print(mn.note.previous())

print(mn.octave_up())
print(mn.octave_above())