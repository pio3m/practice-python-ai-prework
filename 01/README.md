> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `{{kanał-slack}}` (dotyczy [mentee](https://devmentor.pl/mentoring/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#01` Rejestr dokumentów firmy

W tym zadaniu będziesz pracować na rejestrze dokumentów firmy, zapisanym w pliku `data.json`. Plik `starter.py` wczytuje go już do listy słowników `documents`.

Każdy dokument ma pola:
- `id` – identyfikator dokumentu (`str`),
- `type` – rodzaj: `invoice`, `contract` albo `report` (`str`),
- `title` – tytuł (`str`),
- `content` – treść; może być pusta albo zawierać same spacje (`str`),
- `tags` – lista tagów (`list[str]`),
- `pages` – liczba stron (`int`).

Twoje zadania:

1. Policz, ile jest dokumentów każdego rodzaju.
2. Przygotuj alfabetycznie posortowaną listę unikalnych tagów.
3. Zbuduj słownik `id -> title` tylko dla dokumentów, których treść nie jest pusta (treść złożona z samych spacji też jest pusta). Ile elementów ma ten słownik?
4. Wskaż tag, który występuje najczęściej, i podaj liczbę jego wystąpień.
5. Policz łączną liczbę stron wszystkich raportów.

Każdy punkt rozwiąż jednym wyrażeniem (comprehension albo funkcją wbudowaną), bez pętli z `append`.

**Podpowiedź:**  
Zajrzyj do dokumentacji `collections.Counter` (metoda `most_common`), zbiorów (`set`) i metody `str.strip`.

&nbsp;

**Prawidłowe odpowiedzi:**

- **Ad 1:** `invoice`: 5, `report`: 4, `contract`: 3
- **Ad 2:** `['finanse', 'hr', 'it', 'ksiegowosc', 'nieruchomosci', 'poufne', 'prawo', 'rodo', 'zarzad']`
- **Ad 3:** 9
- **Ad 4:** `ksiegowosc`, 5 razy
- **Ad 5:** 38

&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-ai-prework)*

> :arrow_left: ~~*poprzednie zadanie*~~ | [*następne zadanie*](./../02) :arrow_right:
