# Testausdokumentti

Ohjelma on tällä hetkellä testattu yksikkötesteillä, kattavuusraportti löytyy [Codecovista](https://codecov.io/gh/hhautajarvi/kps-tekoaly)

Ohjelman pelivalintojen ja Markovin ketjujen oikeellisuus on testattu yksikkötesteillä antamalla ohjelmalle edellisiä valintoja niin että seuraavaan valintaan on yksi paras vaihtoehto.
Niissä valinnoissa joissa käytetään satunnaisuutta (kun seuraavaan siirtoon on kaksi tai kolme yhtä hyvää vaihtoehtoa) testauksessa on random-funktiolle annettu tietty siemenarvo jolla saadaan aina käytetyistä randint- ja choice-metodeista toistettava paluuarvo.

Oikeellisuutta on samoin testattu myös kehityksen aikana perinteisillä print-debuggaus menetelmillä että on nähty algoritmien ja tietorakenteiden toimivan halutun kaltaisesti.

Pienehkön empiirisen testauksen perusteella tietokone myös voittaa pelaajan hyvin todennäköisesti kun pelejä pelataan jossain määrin merkittävä (>50) määrä.
