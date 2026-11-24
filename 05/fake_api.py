"""Atrapa zewnętrznego API klasyfikującego dokumenty.

Nie modyfikuj tego pliku. Atrapa działa bez internetu: httpx przekazuje
żądanie do funkcji `handle` zamiast wysyłać je w sieć.

API przyjmuje: POST /classify z nagłówkiem `Authorization: Bearer test-key`
i ciałem JSON `{"doc_id": "..."}`. Zwraca JSON `{"doc_id": "...", "label": "..."}`.
"""
import json

import httpx

API_URL = "https://api.example.test"
API_KEY = "test-key"

LABELS = {
    "DOC-001": "invoice",
    "DOC-002": "contract",
    "DOC-003": "report",
    "DOC-004": "invoice",
}
UNAVAILABLE = {"DOC-005"}   # dla tych dokumentów usługa zwraca 503


def handle(request: httpx.Request) -> httpx.Response:
    if request.method != "POST" or request.url.path != "/classify":
        return httpx.Response(404, json={"error": "not found"})
    if request.headers.get("Authorization") != f"Bearer {API_KEY}":
        return httpx.Response(401, json={"error": "invalid api key"})
    try:
        doc_id = json.loads(request.content)["doc_id"]
    except (ValueError, KeyError, TypeError):
        return httpx.Response(400, json={"error": "body must be JSON with doc_id"})
    if doc_id in UNAVAILABLE:
        return httpx.Response(503, json={"error": "service unavailable"})
    if doc_id not in LABELS:
        return httpx.Response(404, json={"error": f"unknown document {doc_id}"})
    return httpx.Response(200, json={"doc_id": doc_id, "label": LABELS[doc_id]})


def fake_transport() -> httpx.MockTransport:
    return httpx.MockTransport(handle)
