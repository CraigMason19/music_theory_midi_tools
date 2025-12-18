
class MIDINote:
    def __init__(self, note: str, octave: int):
        self.note = note
        self.octave = octave

    def __str__(self):
        return f"{self.note}{self.octave}"
    
    def __repr__(self):
        return f"MIDINote({self.note}, {self.octave})"