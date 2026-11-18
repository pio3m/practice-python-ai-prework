> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `{{kanał-slack}}` (dotyczy [mentee](https://devmentor.pl/mentoring/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#04` Model dokumentów firmy

Faktury i umowy różnią się danymi, ale system ma je obsługiwać w jednolity sposób. Twoim zadaniem jest zaprojektować klasy dokumentów, wczytać do nich dane z `documents.json` i przetestować je w pytest.

Klasy do utworzenia w pliku `documents.py`:

- `Document` – klasa abstrakcyjna (dataclass) z polami `doc_id` (`str`), `title` (`str`), `tags` (`list[str]`, domyślnie pusta lista) oraz abstrakcyjną metodą `summary() -> str`,
- `Invoice(Document)` – pola `net_amount` (`float`), `vat_rate` (`float`, domyślnie `0.23`), `due_date` (`date | None`), `paid` (`bool`, domyślnie `False`),
- `Contract(Document)` – pola `party` (`str`), `start_date` (`date`), `end_date` (`date | None`, `None` oznacza umowę bezterminową), `value` (`float`).

Twoim zadaniem jest:

- dodać w `Invoice` właściwość (`@property`) `gross_amount`, czyli kwotę netto powiększoną o VAT, zaokrągloną do 2 miejsc,
- dodać w `Invoice` metodę `is_overdue(today: date) -> bool`: faktura jest po terminie, jeśli nie jest opłacona, a termin jest wcześniejszy niż `today`,
- dodać w `Contract` metodę `is_active(on: date) -> bool`: umowa obowiązuje od `start_date` do `end_date` włącznie,
- zaimplementować `summary()`: dla faktury `Faktura <doc_id>: <brutto> zł brutto`, dla umowy `Umowa <doc_id> z <party>: <value> zł` (kwoty z 2 miejscami po przecinku),
- napisać funkcję `load_documents(path: Path) -> list[Document]`, która tworzy obiekt odpowiedniej klasy na podstawie pola `kind` i zamienia daty z tekstu na `date`,
- napisać `test_documents.py` z fixture zwracającą wczytane dokumenty, testem sprawdzającym, że `Document` nie da się utworzyć (`TypeError`), oraz testem granic dat w `is_active` z użyciem `parametrize`.

**Podpowiedź:**  
Zajrzyj do dokumentacji modułów `dataclasses` (`field`, `default_factory`) i `abc` (`ABC`, `abstractmethod`) oraz dekoratora `@property`. Dekorator `@pytest.fixture` opisuje dokumentacja pytest w rozdziale „How to use fixtures”.

Pole z wartością domyślną w klasie bazowej (`tags`) sprawia, że w klasach pochodnych pole bez wartości domyślnej zgłosi `TypeError: non-default argument ... follows default argument`. Nadaj polom `Invoice` i `Contract` wartości domyślne albo użyj `@dataclass(kw_only=True)`.

&nbsp;

**Prawidłowe odpowiedzi** (data referencyjna: 2026-03-01):

- **Ad 1:** suma kwot brutto wszystkich faktur: 5545.38
- **Ad 2:** faktury po terminie: `FV-001`, `FV-004`
- **Ad 3:** obowiązujące umowy: `UM-001`, `UM-002`
- **Ad 4:** `summary()` dla `FV-003`: `Faktura FV-003: 2951.99 zł brutto`
- **Ad 5:** `summary()` dla `UM-002`: `Umowa UM-002 z Kancelaria Nowak: 3500.00 zł`

&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-ai-prework)*

> :arrow_left: [*poprzednie zadanie*](./../03) | [*następne zadanie*](./../05) :arrow_right:
