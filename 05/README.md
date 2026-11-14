> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `{{kanał-slack}}` (dotyczy [mentee](https://devmentor.pl/mentoring/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#05` Odporny pipeline klasyfikacji dokumentów

Zewnętrzne API klasyfikujące dokumenty bywa niedostępne. Twoim zadaniem jest przetworzyć wszystkie dokumenty z `docs.txt` partiami, równolegle w obrębie partii, z ponawianiem nieudanych prób.

Plik `fake_api.py` symuluje to API. Funkcja `async classify(doc_id: str) -> str` zwraca etykietę (`invoice`, `contract` albo `report`) albo zgłasza `ConnectionError`. Awarie są zapisane w pliku na stałe, więc wynik jest za każdym razem taki sam. Funkcja `total_calls()` zwraca, ile razy wywołano `classify`. Nie modyfikuj tego pliku. Kod piszesz w `starter.py`.

Twoje zadania:

1. Napisz generator `read_batches(path, size)`, który czyta plik linia po linii i zwraca kolejne partie identyfikatorów (listy o długości `size`, ostatnia może być krótsza), pomijając puste linie. Ile jest partii dla `size=5` i ile elementów ma ostatnia?
2. Napisz dekorator `retry(times)` dla funkcji `async`, który po `ConnectionError` ponawia wywołanie, a po `times` nieudanych próbach (liczonych łącznie z pierwszą) zgłasza ostatni wyjątek dalej. Zachowaj nazwę dekorowanej funkcji (`__name__`). Udekoruj nim `classify` z `times=3`.
3. Przetwórz wszystkie partie po 5 dokumentów: każdą partię uruchom przez `asyncio.gather`, tak aby błąd jednego dokumentu nie przerwał pozostałych. Ile dokumentów sklasyfikowano poprawnie i które się nie udały?
4. Ile łącznie razy wywołano `classify` (`total_calls()`) po przetworzeniu wszystkich partii?
5. Ile dokumentów dostało każdą z etykiet?

**Podpowiedź:**  
Zajrzyj do dokumentacji słowa kluczowego `yield`, funkcji `functools.wraps` oraz parametru `return_exceptions` funkcji `asyncio.gather`. Dekorator dla funkcji `async` zwraca funkcję `async`, która używa `await`.

&nbsp;

**Prawidłowe odpowiedzi:**

- **Ad 1:** 5 partii, ostatnia ma 3 elementy
- **Ad 2:** dekorator nie ma wyniku liczbowego; sprawdzisz go w kolejnych punktach
- **Ad 3:** 21 poprawnie, nie udały się `DOC-011` i `DOC-018`
- **Ad 4:** 33 wywołania
- **Ad 5:** `contract`: 8, `report`: 7, `invoice`: 6

&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-ai-prework)*

> :arrow_left: [*poprzednie zadanie*](./../04) | ~~*następne zadanie*~~ :arrow_right:
