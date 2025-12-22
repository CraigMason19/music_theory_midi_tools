
what happens if midi vst cant play a note?
test with midieditor



- play a note via midi
- export a sequence of notes as midi, which can be loaded into 
- midinote.write(duration)




MIDI has 128 notes (0-127), which range from C-1 (negative 1) to G9. A standard piano's 88 keys go from A0 to C8. If your keyboard is setup by default to send the notes of a standard piano, the lowest note should be A0, or MIDI 21, and the highest note will be C8, or MIDI 108.5 Sept 2024



guitar has 0-12. What happens

midi_ranges.py
midi_values.py
????

How can i make a drop c guitar work?
