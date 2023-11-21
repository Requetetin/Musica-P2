from music import *

bassLoop = Score("Bass3", 100)

bass = Part(BASS, 0)
bassNotes =    [C2, D2, E2, F2, E2, D2, C2]
bassDuration = [HN, SN, SN, QN, SN, SN, QN]

## Loop 1
bassPhrase = Phrase()
bassPhrase.addNoteList(bassNotes, bassDuration)
bass.addPhrase(bassPhrase)

bassLoop.addPart(bass)

Play.midi(bassLoop)
Write.midi(bassLoop, "Bass3.mid")


