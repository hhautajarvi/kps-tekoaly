# Käyttöohje

## Ohjelman asentaminen

Asenna riippuvuudet komennolla:

```bash
poetry install
```

Ohjelma käynnistyy komennolla:

```bash
poetry run python3 src/index.py
```

## Ohjelman käyttö

Aluksi ohjelmassa voi valita haluaako pelata normaalia kps:ää valitsemalla 1 tai [spock-lizard- varianttia](https://bigbangtheory.fandom.com/wiki/Rock,_Paper,_Scissors,_Lizard,_Spock) valitsemalla 2. (Variantin toiminallisuus vielä kesken)

Ohjelmaan voi syöttää valintansa seuraavaksi siirroksi pelissä kirjoittamalla tekstikäyttöliittymään joko "kivi" tai "k", "sakset" tai "s" taikka "paperi" tai "p".

Ohjelmasta voi poistua tyhjän rivin kirjoittamalla, eli painamalla vain enteriä.

## Paikallisten testien suorittaminen

Testit voi ajaa komennolla:

```bash
poetry run pytest src
```

Testikattavuusraportin saa komennoilla:

```bash
poetry run coverage run --branch -m pytest
```

```bash
poetry run coverage html
```

Pylintin määrittelemät tyylitarkistukset saa komennolla:

```bash
poetry run pylint src
```
