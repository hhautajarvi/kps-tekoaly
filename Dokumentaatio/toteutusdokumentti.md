# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelman yleisrakenne noudattelee kerrosarkkitehtuuria, jossa tässä on kaksi tasoa, käyttöliittymä ja sovelluslogiikka. Lisäksi käytetyistä tietorakenteista [Trie](https://github.com/hhautajarvi/kps-tekoaly/blob/main/src/datastructures/trie.py) on toteutettu oman luokkanaan.

Käyttöliittymä on toteutettu tekstikäyttöliittymänä, josta huolehtii [console_io](https://github.com/hhautajarvi/kps-tekoaly/blob/main/src/console_io.py) ja käyttöliittymän peliloopista huolehtii [app](https://github.com/hhautajarvi/kps-tekoaly/blob/main/src/app.py).

Sovelluslogiikka on toteutettu kahtena eri luokkana. Itse pelin komentojen muuntamisesta ja tilastojen hoitamisesta huolehtii [game_service](https://github.com/hhautajarvi/kps-tekoaly/blob/main/src/services/game_service.py). Taas pelin ja tietokoneen valintojen logiikasta sekä tietorakenteisiin liittyvästä tallentamisesta huolehtii [logic_service](https://github.com/hhautajarvi/kps-tekoaly/blob/main/src/services/logic_service.py).

## Saavutetut aika- ja tilavaativuudet

Trie-rakenteen toteutuksessa pitäisi olla saavutettu niiden oletetut aika- ja tilavaativuuden, jotka ovat molemmat O(n).
