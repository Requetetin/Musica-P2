# sfx3 Song.py
# Alejandra Gudiel, Diego Alvarez

from music import *

sfx3 = Score("SFX 3", 113)

drumsPart = Part("Drums", 0, 9)

hiHatCHHPhrase = Phrase(0.0)

synthChorus = Part(SYNTH_BASS1, 11)
synthChorus.setTempo(113.0)
synthChorusPhrase = Phrase(0.0)

## synth
synthPitch = [  C4, D4, E4, REST,
                REST, REST, REST, REST,
                C4, D4, E4, REST,
                REST, REST, REST, REST,
            ]
synthDurat = [  SN, SN, EN, DHN,
                QN, QN, QN, QN,
                SN, SN, EN, DHN,
                QN, QN, QN, QN,
                ]
synthChorusPhrase.addNoteList(synthPitch, synthDurat)

## synth 2
synthPitch = [  G2, REST, E3, REST, G4, 
                REST, C4, REST, REST,
                B3, E2, REST, REST, REST,  
                REST, E4, REST, REST,
            ] 
synthDurat = [  QN, SN, DEN, QN, QN,
                QN, QN, QN, QN,
                QN, SN, DEN, QN, QN,
                QN, QN, QN, QN,
                ] 
synthChorusPhrase.addNoteList(synthPitch, synthDurat)

## synth 3
synthPitch = [  G2, REST, 
                REST, E2, REST, REST,
                G3, REST, B3,
                REST, E2,
            ] 
synthDurat = [  DHN, QN,
                QN, QN, QN, QN,
                QN, HN, QN,
                QN, DHN,
                ] 
synthChorusPhrase.addNoteList(synthPitch, synthDurat)


## hiHatCHH
hhtpCHH = [     REST, REST, REST, REST,
                REST, REST, CHH, REST,
                REST, REST, REST, REST,
                REST, REST, CHH, REST
        ] 
hhtdCHH = [     QN, QN, QN, QN,
                QN, QN, EN, QN,
                QN, QN, QN, QN,
                QN, QN, EN, QN,
        ] 
hiHatCHHPhrase.addNoteList(hhtpCHH, hhtdCHH)


drumsPart.addPhrase(hiHatCHHPhrase)
synthChorus.addPhrase(synthChorusPhrase)

sfx3.addPart(synthChorus)
sfx3.addPart(drumsPart)

#View.sketch(sfx3)
Write.midi(sfx3, "sfx3.mid")
Play.midi(sfx3)
