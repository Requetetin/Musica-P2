from music import *

trumpetLoop = Score("Trumpet3", 120)

trumpet = Part(TRUMPET, 0)
trumpetNotes =    [C4, REST, C4, C4, REST, D4, REST, D4, D4]
trumpetDuration = [EN, QN,   SN, SN, QN,   EN, QN,   SN, SN]

## Loop 1
trumpetPhrase = Phrase()
trumpetPhrase.addNoteList(trumpetNotes, trumpetDuration)
trumpet.addPhrase(trumpetPhrase)

trumpetLoop.addPart(trumpet)

Play.midi(trumpetLoop)
Write.midi(trumpetLoop, "Trumpet3.mid")


