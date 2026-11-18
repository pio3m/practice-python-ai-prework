> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `{{kanał-slack}}` (dotyczy [mentee](https://devmentor.pl/mentoring/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#03` Import faktur z katalogu

Księgowość wrzuca faktury do katalogu `data/`: część jako osobne pliki JSON (jedna faktura w pliku), część jako zbiorczy plik CSV. Niektóre pliki są uszkodzone. Twoim zadaniem jest wczytać wszystkie poprawne faktury i przygotować raport.

Każda faktura ma pola:
- `number` – numer faktury (`str`),
- `client` – nazwa klienta (`str`),
- `amount` – kwota brutto (`float`),
- `issue_date` – data wystawienia w formacie ISO, np. `2026-01-05` (`date`),
- `due_date` – termin płatności w formacie ISO (`date`),
- `paid` – czy opłacona; w CSV zapisana jako `true` / `false` (`bool`).

Plik JSON jest uszkodzony, jeśli nie jest poprawnym JSON-em albo brakuje w nim któregokolwiek pola. Uszkodzone pliki pomijasz, ale zapamiętujesz ich nazwy. Program nie może się na nich zatrzymać.

Twoje zadania:

1. Ile faktur udało się poprawnie wczytać (z plików JSON i CSV razem)?
2. Które pliki zostały pominięte jako uszkodzone?
3. Jaka jest łączna kwota nieopłaconych faktur?
4. Która faktura ma najstarszą datę wystawienia?
5. Ile nieopłaconych faktur jest po terminie na dzień 2026-03-01 (termin płatności wcześniejszy niż ta data)? Użyj tej stałej daty, a nie dzisiejszej.
6. Zapisz wyniki do pliku `summary.json` z kluczami `loaded`, `rejected`, `unpaid_total`, `oldest_invoice`, `overdue_count`.

Ścieżki buduj przez `pathlib`, tak aby skrypt działał w Windows, Linux i macOS.

**Podpowiedź:**  
Zajrzyj do dokumentacji `pathlib.Path.glob`, `json.JSONDecodeError`, `csv.DictReader`, `datetime.date.fromisoformat` oraz `json.dump`. Brakujące pole wykryjesz, porównując zbiór wymaganych kluczy z kluczami wczytanego słownika. Uwaga na kolumnę `paid` w CSV: to tekst, a `bool("false")` daje `True`.

&nbsp;

**Prawidłowe odpowiedzi:**

- **Ad 1:** 9 faktur
- **Ad 2:** `FV-2026-005.json`, `FV-2026-006.json`
- **Ad 3:** 11193.5
- **Ad 4:** `FV-2025-118`
- **Ad 5:** 4 faktury
- **Ad 6:** `{"loaded": 9, "rejected": ["FV-2026-005.json", "FV-2026-006.json"], "unpaid_total": 11193.5, "oldest_invoice": "FV-2025-118", "overdue_count": 4}`

&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-ai-prework)*

> :arrow_left: [*poprzednie zadanie*](./../02) | [*następne zadanie*](./../04) :arrow_right:
