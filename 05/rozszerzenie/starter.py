import asyncio
from collections.abc import Iterator
from pathlib import Path

from fake_api import classify, total_calls

DOCS_FILE = Path(__file__).parent / "docs.txt"


def read_batches(path: Path, size: int) -> Iterator[list[str]]:
    # TODO: generator zwracający kolejne partie identyfikatorów (bez pustych linii)
    ...


# TODO: dekorator retry(times) dla funkcji async, ponawiający próbę po ConnectionError


async def main() -> None:
    # TODO: przetwórz partie po 5 dokumentów, każdą przez asyncio.gather
    ...


if __name__ == "__main__":
    asyncio.run(main())
