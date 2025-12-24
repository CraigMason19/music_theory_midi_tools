from typing import Self

from music_theory import Note

class MIDINote():
    def __init__(self, note: Note, octave: int):
        self.note = note
        self.octave = octave

    def octave_up(self) -> Self:
        return MIDINote(self.note, self.octave + 1)

    octave_above = octave_up # Alias

    def octave_down(self) -> Self:
        return MIDINote(self.note, self.octave - 1)

    octave_below = octave_down # Alias

    def __str__(self) -> str:
        return f"{self.note}{self.octave}"
    
    def __repr__(self) -> str:
        return f"MIDINote({repr(self.note)}, {self.octave})"
    

MIDDLE_C = MIDINote(Note.C, 4)