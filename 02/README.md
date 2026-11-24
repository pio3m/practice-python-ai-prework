> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `{{kanał-slack}}` (dotyczy [mentee](https://devmentor.pl/mentoring/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#02` Parser kwot z faktur

Kwoty z faktur trafiają do systemu jako tekst wpisany przez ludzi, więc mają różny format. Twoim zadaniem jest napisać parser, który przyjmuje poprawne kwoty i odrzuca resztę, oraz przetestować go w pytest.

Poprawna kwota:
- może mieć na początku i na końcu spacje, które się pomija,
- może kończyć się oznaczeniem waluty `zł` (ze spacją przed nim lub bez); inna waluta (np. `EUR`) jest błędem,
- składa się wyłącznie z cyfr ASCII `0–9`, opcjonalnych spacji jako separatora tysięcy i co najwyżej jednego separatora dziesiętnego: przecinka albo kropki,
- spacje tysięcy dzielą liczbę na poprawne grupy: pierwsza ma 1–3 cyfry, każda kolejna dokładnie 3 (`1 000 000` jest poprawne, `12 34` nie),
- ma 1 albo 2 cyfry po separatorze dziesiętnym (jeśli separator występuje),
- nie może być pusta ani ujemna.

Wszystko inne odrzucasz, w tym `nan`, `inf`, zapis wykładniczy (`1e3`) i liczby ze znakiem `-` albo `+`. Uwaga: funkcja `float()` sama przyjmuje `"nan"`, `"inf"` i `"1e3"`, więc najpierw sprawdź format, a dopiero potem zamieniaj tekst na liczbę.

> Typ `float` służy tu do nauki. W prawdziwym systemie księgowym kwoty przechowuje się jako `Decimal` albo liczbę groszy.

Twoim zadaniem jest:

- utworzyć plik `amounts.py` z wyjątkiem `InvalidAmountError`, który dziedziczy po `ValueError`,
- napisać w nim funkcję `parse_amount(raw: str) -> float`, która zwraca kwotę albo zgłasza `InvalidAmountError` z komunikatem zawierającym błędny tekst,
- napisać funkcję `parse_many(raws: list[str]) -> tuple[list[float], list[str]]`, która zwraca listę poprawnych kwot i listę komunikatów błędów; łapie **tylko** `InvalidAmountError` (inne błędy, np. przekazanie liczby zamiast tekstu, mają być widoczne),
- utworzyć plik `test_amounts.py` z co najmniej 6 testami: użyj `@pytest.mark.parametrize` dla poprawnych i dla błędnych kwot oraz `pytest.raises`; wyniki typu `float` porównuj przez `pytest.approx`,
- wczytać plik `amounts.txt` (każda linia, również pusta, to jedna pozycja) i odpowiedzieć na pytania poniżej.

**Podpowiedź:**  
Przydadzą się metody `str.strip` i `str.endswith` oraz funkcja `re.fullmatch` z wzorcem dla grup tysięcy (sekcja 0.3). Testy uruchomisz komendą `python -m pytest -v` (albo `uv run python -m pytest -v`).

&nbsp;

**Prawidłowe odpowiedzi:**

- **Ad 1:** plik ma 16 pozycji
- **Ad 2:** 9 kwot jest poprawnych
- **Ad 3:** suma poprawnych kwot to 1004199.06
- **Ad 4:** 7 pozycji jest błędnych

&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-ai-prework)*

> :arrow_left: [*poprzednie zadanie*](./../01) | [*następne zadanie*](./../03) :arrow_right:
