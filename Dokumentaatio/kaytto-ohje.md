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

Ohjelmaan voi tällä hetkellä syöttää valintansa seuraavaksi siirroksi pelissä kirjoittamalla tekstikäyttöliittymään joko "kivi" tai "k", "sakset" tai "s" taikka "paperi" tai "p".

Ohjelmasta voi poistua tyhjän rivin kirjoittamalla, eli painamalla vain enteriä.

## Paikallisten testien suorittaminen

Testit voi ajaa komennolla (pelkkä "pytest src" ei tällä hetkellä toimi koska ei jostain syystä löydä import-polkua):

```bash
poetry run coverage run --branch -m pytest
```

Testikattavuusraportin saa komennoilla

```bash
poetry run coverage html
```

Pylintin määrittelemät tyylitarkistukset saa komennolla:

```bash
poetry run pylint src
```
