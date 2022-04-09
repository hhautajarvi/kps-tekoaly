# Testausdokumentti

## Yksikkötestaus ja oikeellisuus

Ohjelma on tällä hetkellä testattu yksikkötesteillä, kattavuusraportti löytyy [Codecovista](https://codecov.io/gh/hhautajarvi/kps-tekoaly)

Ohjelman pelivalintojen ja Markovin ketjujen oikeellisuus on testattu yksikkötesteillä antamalla ohjelmalle edellisiä valintoja niin että seuraavaan valintaan on yksi paras vaihtoehto.
Niissä valinnoissa joissa käytetään satunnaisuutta (kun seuraavaan siirtoon on kaksi tai kolme yhtä hyvää vaihtoehtoa) testauksessa on random-funktiolle annettu tietty siemenarvo jolla saadaan aina käytetyistä randint- ja choice-metodeista toistettava paluuarvo.

Oikeellisuutta on samoin testattu myös kehityksen aikana perinteisillä print-debuggaus menetelmillä että on nähty algoritmien ja tietorakenteiden toimivan halutun kaltaisesti.

## Empiirinen testaus

Pienehkön empiirisen testauksen perusteella tietokone myös voittaa pelaajan hyvin todennäköisesti kun pelejä pelataan jossain määrin merkittävä (>50) määrä.

Jos pelaaja tietää tietokoneen valintatavan ja yrittää pelata sitä vastaan pitämällä mielessään kirjaa jollain tasolla siirroistaan ja vaihtelemalla usein valintametodiaan, pelaajalla on kuitenkin hyvä mahdollisuus voittaa. Tämä toki selvästi vaikeutuu mitä pidemmälle peliä pelataan ja alkaa kokeiltaessa helposti tasoittumaan jossain >200 pelatun pelin jälkeen.
