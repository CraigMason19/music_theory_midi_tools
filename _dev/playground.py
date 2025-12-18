import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from music_theory_midi_tools.midi_note import MIDINote



mn = MIDINote("C", "4")


print(mn)