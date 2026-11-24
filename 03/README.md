> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `{{kanał-slack}}` (dotyczy [mentee](https://devmentor.pl/mentoring/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#03` Import faktur z katalogu

Księgowość wrzuca faktury do katalogu `data/` jako osobne pliki JSON: jedna faktura w jednym pliku. Niektóre pliki są uszkodzone. Twoim zadaniem jest wczytać wszystkie poprawne faktury i przygotować proste podsumowanie.

Każda faktura ma pola:
- `number` – numer faktury (`str`),
- `client` – nazwa klienta (`str`),
- `amount` – kwota brutto (`float`),
- `issue_date` – data wystawienia jako tekst, np. `"2026-01-05"` (`str`),
- `due_date` – termin płatności jako tekst (`str`),
- `paid` – czy opłacona (`bool`).

Plik jest uszkodzony, jeśli nie jest poprawnym JSON-em albo brakuje w nim któregokolwiek pola. Uszkodzone pliki pomijasz, ale zapamiętujesz ich nazwy. Program nie może się na nich zatrzymać.

Wczytuj tylko pliki `*.json`, **w kolejności posortowanej po nazwie** (inne pliki w katalogu ignorujesz). Zachowanie w przypadkach brzegowych:
- brak katalogu: czytelny błąd (np. `FileNotFoundError` z nazwą katalogu),
- pusty katalog: 0 wczytanych faktur i pusta lista pominiętych plików, bez wyjątku.

Twoje zadania:

1. Ile faktur udało się poprawnie wczytać?
2. Które pliki zostały pominięte jako uszkodzone?
3. Jaka jest łączna kwota nieopłaconych faktur?
4. Która faktura ma najwyższą kwotę?
5. Zapisz wyniki do pliku `summary.json` z kluczami `loaded`, `rejected`, `unpaid_total`, `largest_invoice`.

Ścieżki buduj przez `pathlib`, pliki otwieraj przez `with` z `encoding="utf-8"`, tak aby skrypt działał w Windows, Linux i macOS.

**Podpowiedź:**  
Przyda się `Path.glob`, `sorted`, `json.load`, `json.JSONDecodeError` i `json.dump` (z `ensure_ascii=False` i `indent=2`). Brakujące pole wykryjesz, sprawdzając dla każdego wymaganego klucza, czy jest w słowniku (`klucz in faktura`).

&nbsp;

**Prawidłowe odpowiedzi:**

- **Ad 1:** 4 faktury
- **Ad 2:** `FV-2026-005.json`, `FV-2026-006.json`
- **Ad 3:** 5535.0
- **Ad 4:** `FV-2026-003`
- **Ad 5:** `{"loaded": 4, "rejected": ["FV-2026-005.json", "FV-2026-006.json"], "unpaid_total": 5535.0, "largest_invoice": "FV-2026-003"}`

&nbsp;

**Rozszerzenie (opcjonalne): CSV i daty**

W katalogu `data/` jest też zbiorczy plik `import-luty.csv` z kolejnymi fakturami. Rozbuduj import:

1. Wczytaj faktury z plików JSON i CSV razem (`csv.DictReader`). Uwaga na kolumnę `paid`: to tekst, a `bool("false")` daje `True`.
2. Zamień daty na `date` przez `datetime.date.fromisoformat`.
3. Policz łączną kwotę nieopłaconych faktur, wskaż fakturę z najstarszą datą wystawienia i policz nieopłacone faktury po terminie na dzień 2026-03-01 (termin wcześniejszy niż ta data). Użyj tej stałej daty, a nie dzisiejszej.

Odpowiedzi do rozszerzenia: 9 faktur razem, nieopłacone 11193.5, najstarsza `FV-2025-118`, po terminie 4 faktury.

&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-ai-prework)*

> :arrow_left: [*poprzednie zadanie*](./../02) | [*następne zadanie*](./../04) :arrow_right:
