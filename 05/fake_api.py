"""Symulacja zawodnego zewnętrznego API klasyfikującego dokumenty.

Nie modyfikuj tego pliku. Awarie są zapisane na stałe, więc wynik jest
za każdym razem taki sam.
"""
import asyncio

# Ile pierwszych wywołań dla danego dokumentu kończy się ConnectionError.
FAILURES: dict[str, int] = {
    "DOC-003": 1,
    "DOC-007": 2,
    "DOC-011": 5,
    "DOC-014": 1,
    "DOC-018": 3,
    "DOC-022": 2,
}

LABELS = ("invoice", "contract", "report")

calls: dict[str, int] = {}


def total_calls() -> int:
    """Łączna liczba wywołań classify od uruchomienia programu."""
    return sum(calls.values())


async def classify(doc_id: str) -> str:
    calls[doc_id] = calls.get(doc_id, 0) + 1
    await asyncio.sleep(0.01)
    if calls[doc_id] <= FAILURES.get(doc_id, 0):
        raise ConnectionError(f"API niedostępne dla {doc_id}")
    number = int(doc_id.split("-")[1])
    return LABELS[number % len(LABELS)]
