from music import *

bassLoop = Score("Bass2", 60)

bass = Part(BASS, 0)
bassNotes =    [C2, C2, C2, F2, F2, F2, A2, B2, G2, DS2]
bassDuration = [HN, SN, SN, HN, EN, EN, QN, EN, SN, QN]

## Loop 1
bassPhrase = Phrase()
bassPhrase.addNoteList(bassNotes, bassDuration)
bass.addPhrase(bassPhrase)

bassLoop.addPart(bass)

Play.midi(bassLoop)
Write.midi(bassLoop, "Bass2.mid")


