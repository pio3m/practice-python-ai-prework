import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data.json"

with DATA_FILE.open(encoding="utf-8") as file:
    documents: list[dict] = json.load(file)

# TODO: Ad 1, liczba dokumentów każdego typu
# TODO: Ad 2, posortowana lista unikalnych tagów
# TODO: Ad 3, słownik id -> tytuł dla dokumentów z niepustą treścią
# TODO: Ad 4, najczęstszy tag i liczba jego wystąpień
# TODO: Ad 5, łączna liczba stron wszystkich raportów
