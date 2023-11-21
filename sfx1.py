# sfx1 Song.py
# Alejandra Gudiel, Diego Alvarez

from music import *

sfx1 = Score("SFX 1", 113)

drumsPart = Part("Drums", 0, 9)
hiHatCHHPhrase = Phrase(0.0)

synthChorus = Part(SYNTH_BASS1, 11)
synthChorus.setTempo(113.0)
synthChorusPhrase = Phrase(0.0)

synthChorus2 = Part(SYNTH_BASS2, 12)
synthChorus2.setTempo(113.0)
synthChorusPhrase2 = Phrase(0.0)

## synth
synthPitch = [  F4, D3, F4, D3, 
                F4, D3, F4, D3, 
                F4, D3, F4, D3, 
                F4, D3, F4, D3, 
            ]
synthDurat = [  QN, QN, QN, QN,
                QN, QN, QN, QN,
                QN, QN, QN, QN,
                QN, QN, QN, QN,
                ]
synthChorusPhrase.addNoteList(synthPitch, synthDurat)

## synth 2
synthPitch = [  E4, C4, REST, C4, 
                E4, C4, E4, C4, 
                E4, C4, REST, C4, 
                E4, C4, E4, C4, 
            ] 
synthDurat = [  QN, QN, QN, QN,
                QN, QN, QN, QN,
                QN, QN, QN, QN,
                QN, QN, QN, QN,
                ] 
synthChorusPhrase.addNoteList(synthPitch, synthDurat)


## hiHatCHH
hhtpCHH = [        CHH, CHH, CHH, REST, 
                CHH, CHH, CHH, REST,
                CHH, CHH, CHH, REST,
                CHH, CHH, CHH, REST
        ] * 2
hhtdCHH = [        EN, EN, EN, EN,
                EN, EN, EN, EN,
                EN, EN, EN, EN,
                EN, EN, EN, EN,
        ] * 2
hiHatCHHPhrase.addNoteList(hhtpCHH, hhtdCHH)


drumsPart.addPhrase(hiHatCHHPhrase)
synthChorus.addPhrase(synthChorusPhrase)
synthChorus2.addPhrase(synthChorusPhrase2)

sfx1.addPart(synthChorus)
sfx1.addPart(synthChorus2)
sfx1.addPart(drumsPart)

#View.sketch(sfx1)
#Write.midi(sfx1, "sfx1.mid")
Play.midi(sfx1)
