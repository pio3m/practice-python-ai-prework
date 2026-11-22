> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `{{kanał-slack}}` (dotyczy [mentee](https://devmentor.pl/mentoring/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#02` Parser kwot z faktur

Kwoty z faktur trafiają do systemu jako tekst wpisany przez ludzi, więc mają różny format. Twoim zadaniem jest napisać parser, który przyjmuje poprawne kwoty i odrzuca resztę, oraz przetestować go w pytest.

Poprawna kwota:
- może mieć na początku i na końcu spacje, które się pomija,
- może kończyć się oznaczeniem waluty `zł` (ze spacją przed nim lub bez),
- może zawierać spacje jako separator tysięcy (`1 000 000`),
- poza tym składa się wyłącznie z cyfr i co najwyżej jednego separatora dziesiętnego: przecinka albo kropki,
- ma najwyżej 2 cyfry po separatorze dziesiętnym,
- nie może być pusta ani ujemna.

Twoim zadaniem jest:

- utworzyć plik `amounts.py` z wyjątkiem `InvalidAmountError`, który dziedziczy po `ValueError`,
- napisać w nim funkcję `parse_amount(raw: str) -> float`, która zwraca kwotę albo zgłasza `InvalidAmountError` z komunikatem zawierającym błędny tekst,
- napisać funkcję `parse_many(raws: list[str]) -> tuple[list[float], list[str]]`, która zwraca listę poprawnych kwot i listę komunikatów błędów, a sama nigdy nie zgłasza wyjątku,
- utworzyć plik `test_amounts.py` z co najmniej 6 testami: użyj `@pytest.mark.parametrize` dla poprawnych i dla błędnych kwot oraz `pytest.raises`,
- wczytać plik `amounts.txt` (każda linia, również pusta, to jedna pozycja) i odpowiedzieć na pytania poniżej.

**Podpowiedź:**  
Przydadzą się metody `str.strip`, `str.endswith` i `str.replace`. Sprawdzanie formatu możesz oprzeć na `str.isdigit` albo na module `re` (funkcja `re.fullmatch`). Testy uruchomisz komendą `pytest -v`. Tych metod i modułu `re` nie było na slajdach: to celowe ćwiczenie w samodzielnym czytaniu dokumentacji Pythona.

&nbsp;

**Prawidłowe odpowiedzi:**

- **Ad 1:** plik ma 16 pozycji
- **Ad 2:** 9 kwot jest poprawnych
- **Ad 3:** suma poprawnych kwot to 1004199.06
- **Ad 4:** 7 pozycji jest błędnych

&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-ai-prework)*

> :arrow_left: [*poprzednie zadanie*](./../01) | [*następne zadanie*](./../03) :arrow_right:
