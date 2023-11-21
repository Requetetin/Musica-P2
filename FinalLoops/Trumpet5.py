from music import *

trumpetLoop = Score("Trumpet5", 120)

trumpet = Part(TRUMPET, 0)
trumpetNotes =    [C4, REST, D4, REST, C4, REST, B3, REST]
trumpetDuration = [QN, QN,  QN,  QN,   QN, QN,   QN, QN]

## Loop 1
trumpetPhrase = Phrase()
trumpetPhrase.addNoteList(trumpetNotes, trumpetDuration)
trumpet.addPhrase(trumpetPhrase)

trumpetLoop.addPart(trumpet)

Play.midi(trumpetLoop)
Write.midi(trumpetLoop, "Trumpet5.mid")


