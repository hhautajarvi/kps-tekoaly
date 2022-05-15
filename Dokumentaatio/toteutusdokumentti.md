# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelman yleisrakenne noudattelee kerrosarkkitehtuuria, jossa tässä on kaksi tasoa, käyttöliittymä ja sovelluslogiikka. Lisäksi käytetyistä tietorakenteista [Trie](https://github.com/hhautajarvi/kps-tekoaly/blob/main/src/datastructures/trie.py) on toteutettu oman luokkanaan.

[Index.py](https://github.com/hhautajarvi/kps-tekoaly/blob/main/src/index.py) hoitaa ohjelman käynnistyksen ja riippuvuuksien injektoinnin käyttöliittymään.

Käyttöliittymä on toteutettu tekstikäyttöliittymänä, josta huolehtii [console_io](https://github.com/hhautajarvi/kps-tekoaly/blob/main/src/console_io.py) ja käyttöliittymän peliloopista huolehtii [app](https://github.com/hhautajarvi/kps-tekoaly/blob/main/src/app.py).

Sovelluslogiikka on toteutettu kahtena eri luokkana. Itse pelin komentojen muuntamisesta ja tilastojen hoitamisesta huolehtii [game_service](https://github.com/hhautajarvi/kps-tekoaly/blob/main/src/services/game_service.py). Taas pelin ja tietokoneen valintojen logiikasta sekä tietorakenteisiin liittyvästä tallentamisesta huolehtii [logic_service](https://github.com/hhautajarvi/kps-tekoaly/blob/main/src/services/logic_service.py).

## Saavutetut aika- ja tilavaativuudet

Trie-rakenteen toteutuksessa pitäisi olla saavutettu niiden oletetut aika- ja tilavaativuuden, jotka ovat molemmat O(1).

## Parannusideat

Ohjelmaan olisi vielä voinut kehittää enemmän erilaisia pelaajan käytöksiä etsiviä Markovin ketjuja. Näin olisi voitu ehkä parantaa ohjelman toimivuutta silloin kuin pelaaja tietää tai oppii tietokoneen toimintatavan, sekä pienillä pelimäärillä parantaa tietokoneen voittomääriä.

## Lähteet

Lähteenä ja perusideana ohjelmalle on käytetty seuraavaa artikkelia: [Wang et. al., Multi‑AI competing and winning against humans in iterated Rock‑Paper‑Scissors game](https://arxiv.org/pdf/2003.06769.pdf)
