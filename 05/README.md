> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `{{kanał-slack}}` (dotyczy [mentee](https://devmentor.pl/mentoring/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#05` Klasyfikacja dokumentu przez API (HTTP i async)

Aplikacja wysyła dokument do zewnętrznego API, które zwraca jego rodzaj (`invoice`, `contract` albo `report`). Tak samo w Module 1 będziesz wywoływać API modelu językowego. Twoim zadaniem jest uzupełnić gotowy szkielet **jednego asynchronicznego wywołania POST**.

Plik `fake_api.py` to atrapa API: działa bez internetu i bez prawdziwych kluczy (`httpx.MockTransport`). Nie modyfikuj go. Kod piszesz w `starter.py`, w funkcji `classify_document`.

API:
- przyjmuje `POST /classify` z ciałem JSON `{"doc_id": "DOC-001"}` i nagłówkiem `Authorization` (klient w `make_client` dodaje go za Ciebie),
- przy sukcesie zwraca status `200` i JSON `{"doc_id": "DOC-001", "label": "invoice"}`,
- przy błędnym kluczu zwraca `401`, a gdy usługa jest chwilowo niedostępna `503`.

Twoje zadania:

1. Uzupełnij `classify_document`: wyślij żądanie przez `await client.post(...)`, wywołaj `raise_for_status()` **przed** odczytem `.json()` i zwróć pole `label`.
2. Błąd statusu HTTP (`httpx.HTTPStatusError`) zamień na `ClassificationError` z komunikatem `<doc_id>: HTTP <kod>`, np. `DOC-005: HTTP 503`. Nie łap innych wyjątków.
3. Uruchom program (`python starter.py`). Jakie etykiety dostały `DOC-001`, `DOC-002` i `DOC-003`?
4. Jaki komunikat błędu wypisał program dla `DOC-005`?
5. Uruchom gotowe testy pomocnicze (`python -m pytest -v`). Ile testów przechodzi?

**Podpowiedź:**  
Wróć do slajdów sekcji 0.8: `async def`, `await`, `async with httpx.AsyncClient(...)`, `raise_for_status()` i `MockTransport`. Kod statusu odczytasz z wyjątku: `err.response.status_code`.

&nbsp;

**Prawidłowe odpowiedzi:**

- **Ad 3:** `DOC-001`: `invoice`, `DOC-002`: `contract`, `DOC-003`: `report`
- **Ad 4:** `Błąd: DOC-005: HTTP 503`
- **Ad 5:** 3 testy (`3 passed`)

&nbsp;

**Rozszerzenie (opcjonalne): odporny pipeline z generatorem, retry i `asyncio.gather`**

Zewnętrzne API klasyfikujące dokumenty bywa niedostępne. Twoim zadaniem jest przetworzyć wszystkie dokumenty z `rozszerzenie/docs.txt` partiami, równolegle w obrębie partii, z ponawianiem nieudanych prób.

Pliki znajdziesz w katalogu `rozszerzenie/`. Plik `rozszerzenie/fake_api.py` symuluje to API. Funkcja `async classify(doc_id: str) -> str` zwraca etykietę (`invoice`, `contract` albo `report`) albo zgłasza `ConnectionError`. Awarie są zapisane w pliku na stałe, więc wynik jest za każdym razem taki sam. Funkcja `total_calls()` zwraca, ile razy wywołano `classify`. Nie modyfikuj tego pliku. Kod piszesz w `rozszerzenie/starter.py`.

Twoje zadania:

1. Napisz generator `read_batches(path, size)`, który czyta plik linia po linii i zwraca kolejne partie identyfikatorów (listy o długości `size`, ostatnia może być krótsza), pomijając puste linie. Ile jest partii dla `size=5` i ile elementów ma ostatnia?
2. Napisz dekorator `retry(times)` dla funkcji `async`, który po `ConnectionError` ponawia wywołanie, a po `times` nieudanych próbach (liczonych łącznie z pierwszą) zgłasza ostatni wyjątek dalej. Zachowaj nazwę dekorowanej funkcji (`__name__`). Udekoruj nim `classify` z `times=3`.
3. Przetwórz wszystkie partie po 5 dokumentów: każdą partię uruchom przez `asyncio.gather`, tak aby błąd jednego dokumentu nie przerwał pozostałych. Ile dokumentów sklasyfikowano poprawnie i które się nie udały?
4. Ile łącznie razy wywołano `classify` (`total_calls()`) po przetworzeniu wszystkich partii?
5. Ile dokumentów dostało każdą z etykiet?

**Podpowiedź:**  
Zajrzyj do dokumentacji słowa kluczowego `yield`, funkcji `functools.wraps` oraz parametru `return_exceptions` funkcji `asyncio.gather`. Dekorator dla funkcji `async` zwraca funkcję `async`, która używa `await`.

&nbsp;

Odpowiedzi do rozszerzenia:

- **Ad 1:** 5 partii, ostatnia ma 3 elementy
- **Ad 2:** dekorator nie ma wyniku liczbowego; sprawdzisz go w kolejnych punktach
- **Ad 3:** 21 poprawnie, nie udały się `DOC-011` i `DOC-018`
- **Ad 4:** 33 wywołania
- **Ad 5:** `contract`: 8, `report`: 7, `invoice`: 6

&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-ai-prework)*

> :arrow_left: [*poprzednie zadanie*](./../04) | ~~*następne zadanie*~~ :arrow_right:
