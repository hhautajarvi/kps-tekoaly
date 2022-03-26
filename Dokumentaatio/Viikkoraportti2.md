# Viikkoraportti 2

Tällä viikolla olen saanut pelin alustavan pohjan tehtyä, olen implementoinut siihen valmiin trie-toteutuksen pohjalle ja tehnyt alustavan toteutuksen 2-asteen Markovin ketjuista.

## Seuraavaksi tehtävää

Seuraavaksi pitäisi useamman asteen vastaavat Markovin ketjut ja niiden vertailu kuinka hyvin ne sopivat mikäkin malliksi edellisten siirtojen (esim. 5 kappaletta) perusteella. Näin algoritmi valitsisi todennäköisimmin parhaan algoritmin seuraavaksi.

## Epäselväksi jäänyttä

Hieman jäi mietityttämään että onko Markovin ketjun toteutus oikean suuntainen varmasti [(game_service.py cpu_choice)](https://github.com/hhautajarvi/kps-tekoaly/blob/main/src/services/game_service.py). Eli nyt se vain tutkii mikä on kahden edellisen siirron perusteella ollut yleisin siirto aikaisemmin, jos niitä on ollut kaksi yhtä usein niin silloin arvotaan näiden väliltä. Muuten valinta arvotaa täysin.

Samoin Triehen tallennettavat ketjut mietityttävät että ovatko ne fiksusti toteutettu (game_service.py add_choice). Eli esim. nyt jos on viiden ketju [vanhin, toinen, kolmas, neljäs, uusin] niin sinne tallennetaan tuon lisäksi [toinen, kolmas, neljäs, uusin], [kolmas, neljäs, uusin], [neljäs, uusin] ja [uusin].

Myös en aluksi huomannut materiaaleissa että kaikki koodi pitäisi tehdä samalla kielellä kuin dokumentaatiot, onko suurta väliä vaikka koodin kieli on englanti. Muilla kursseilla tähän on kehoitettu ja se tulee jo aika selkäytimestä. Onko tästä siis haittaa jos kommentit yms. on kuitenkin suomeksi?

## Tuntikirjanpito

|Päivä| Aika (h) | Mitä tein |
| :----:|:-----| :-----|
|18.3.| 5 | Aiheisiin ja kurssimateriaaliin tutustumista ja oman aiheen valinta|
|19.3.| 3 | Omaan aiheeseen tutustumista, dokumentaation aloittaminen|
|25.3.| 4 | Työn pohjan tekeminen ja suunnittelu|
|26.3.| 7 | Triehen ja Markoviin ketjuihin tutustumista ja niiden alustava toteutus ja testauksen aloitus|
