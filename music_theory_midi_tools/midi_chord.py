from music_theory_midi_tools.midi_note import MIDINote

class MIDIChord:
    def __init__(self, chord: str):
        self.chord = chord
        self.midi_notes = [MIDINote(note, 4) for note in chord.notes]

    def __str__(self):
        return f"{str(self.chord)}"
    
    def __repr__(self):
        return f"MIDIChord({str(self.chord)}, {[str(note) for note in self.midi_notes]})"