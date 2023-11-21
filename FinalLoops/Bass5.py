from music import *

bassLoop = Score("Bass5", 120)

bass = Part(BASS, 0)
bassNotes =    [C2, C2, C2, F2, F2, F2, A2, B2, G2, DS2, G2, B2, A2, F2, F2, F2, C2, C2, C2]
bassDuration = [HN, SN, SN, HN, EN, EN, QN, EN, SN, QN,  SN, EN, QN, EN, EN, HN, SN, SN, HN]

## Loop 1
bassPhrase = Phrase()
bassPhrase.addNoteList(bassNotes, bassDuration)
bass.addPhrase(bassPhrase)

bassLoop.addPart(bass)

Play.midi(bassLoop)
Write.midi(bassLoop, "Bass5.mid")


