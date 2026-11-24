import asyncio

import httpx

from fake_api import API_KEY, API_URL, fake_transport


class ClassificationError(Exception):
    """Nie udało się sklasyfikować dokumentu."""


async def classify_document(client: httpx.AsyncClient, doc_id: str) -> str:
    # TODO: wyślij POST na "/classify" z ciałem JSON {"doc_id": doc_id} (pamiętaj o await),
    #       sprawdź status przez raise_for_status() i zwróć pole "label" z odpowiedzi JSON.
    # TODO: błąd statusu HTTP (httpx.HTTPStatusError) zamień na ClassificationError
    #       z komunikatem w formacie "<doc_id>: HTTP <kod statusu>".
    ...


def make_client(api_key: str = API_KEY) -> httpx.AsyncClient:
    return httpx.AsyncClient(
        base_url=API_URL,
        transport=fake_transport(),
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=5.0,
    )


async def main() -> None:
    async with make_client() as client:
        for doc_id in ["DOC-001", "DOC-002", "DOC-003", "DOC-005"]:
            try:
                label = await classify_document(client, doc_id)
                print(f"{doc_id}: {label}")
            except ClassificationError as err:
                print(f"Błąd: {err}")


if __name__ == "__main__":
    asyncio.run(main())
