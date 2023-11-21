# sfx2 Song.py
# Alejandra Gudiel, Diego Alvarez

from music import *

sfx2 = Score("SFX 2", 113)

drumsPart = Part("Drums", 0, 9)
hiHatCHHPhrase = Phrase(0.0)

synthChorus = Part(SYNTH_BASS1, 11)
synthChorus.setTempo(113.0)
synthChorusPhrase = Phrase(0.0)

## synth
synthPitch = [  B3, A3, G3, F3, G3, E3, 
                B3, A3, G3, F3, G3, E3,
                B3, A3, G3, F3, G3, E3,
                B3, A3, G3, F3, G3, E3,
            ]
synthDurat = [  EN, EN, EN, DQN, QN, QN,
                EN, EN, EN, DQN, QN, QN,
                EN, EN, EN, DQN, QN, QN,
                EN, EN, EN, DQN, QN, QN,
                ]
synthChorusPhrase.addNoteList(synthPitch, synthDurat)

## synth 2
synthPitch = [  B2, E3, REST, G4, 
                E4, C4, E4, C4, 
                B2, E3, REST, G4,  
                E4, C4, E4, C4, 
            ] 
synthDurat = [  EN, EN, HN, QN,
                EN, EN, HN, QN,
                EN, EN, HN, QN,
                EN, EN, HN, QN,
                ] 
synthChorusPhrase.addNoteList(synthPitch, synthDurat)


## hiHatCHH
hhtpCHH = [     CHH, CHH, CHH, REST, 
                CHH, CHH, CHH, REST,
                CHH, CHH, CHH, REST,
                CHH, CHH, CHH, REST
        ] * 2
hhtdCHH = [     EN, EN, EN, EN,
                EN, EN, EN, EN,
                EN, EN, EN, EN,
                EN, EN, EN, EN,
        ] * 2
hiHatCHHPhrase.addNoteList(hhtpCHH, hhtdCHH)


drumsPart.addPhrase(hiHatCHHPhrase)
synthChorus.addPhrase(synthChorusPhrase)

sfx2.addPart(synthChorus)
# sfx2.addPart(drumsPart)

#View.sketch(sfx2)
Write.midi(sfx2, "sfx2.mid")
Play.midi(sfx2)
