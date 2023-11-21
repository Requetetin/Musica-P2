from music import *

trumpetLoop = Score("Trumpet1", 120)

trumpet = Part(TRUMPET, 0)
trumpetNotes =    [G4, A4, B4, C5, B4, A4, G4, A4, G4]
trumpetDuration = [HN, EN, EN, HN, SN, SN, QN, HN, WN]

## Loop 1
trumpetPhrase = Phrase()
trumpetPhrase.addNoteList(trumpetNotes, trumpetDuration)
trumpet.addPhrase(trumpetPhrase)

trumpetLoop.addPart(trumpet)

Play.midi(trumpetLoop)
Write.midi(trumpetLoop, "Trumpet1.mid")


