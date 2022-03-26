# Määrittelydokumentti

Työssä on tarkoitus toteuttaa tekoäly joka pelaa ihmistä vastaan kivi-paperi-sakset -peliä iteratiivisesti monia kierroksia ja yrittää valita ihmisen käytöksen mukaan useammasta mallista toimivimman seuraavaan siirtoon. Ohjelma toteutetaan Pythonilla.

## Käytettävät algoritmit ja tietorakenteet

Tekoäly käyttää eripituisia Markovin ketjuja pelaajan käytöksen tunnistamiseksi ja käyttää aikaisempiin peleihin parhaiten sopinutta mallia seuraavaan kierrokseen.

Tietorakenteena käytetään trie-rakennetta, johon tallennetaan pelaajan aikaisemmin pelaamat siirrot merkkijonoina ja niiden frekvenssit.

## Syötteet ja niiden käyttö

Ohjelmaa käytetään tekstipohjaisella käyttöliittymällä. Pelin ollessa käynnissä peli saa pelaajalta saa syötteenä seuraavan siirron (kivi, paperi tai sakset), jonka jälkeen peli paljastaa oman valintansa ja voittaja selviää. Peliä on tarkoitus jatkaa mielellään kymmeniä kierroksia, jotta saadaan sopiva tilastollinen otoskoko.

## Aika- ja tilavaativuudet

Trie-rakenteen aika- ja tilavaativuudet ovat aina O(n).

## Lähteet

Tekoälyn pohja-idea: [Wang et. al., Multi‑AI competing and winning against humans in iterated Rock‑Paper‑Scissors game](https://arxiv.org/pdf/2003.06769.pdf)

Trie-tietorakenne: [Trie, Wikipedia](https://en.wikipedia.org/wiki/Trie)

## Lisätiedot

Opinto-ohjelma: Tietojenkäsittelytieteen kanditaatti (TKT)

Dokumentaation kieli: Suomi

Hallitut ohjelmointikielet: Python
