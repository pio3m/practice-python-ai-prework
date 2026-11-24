"""Gotowe testy pomocnicze do zadania #05. Uruchom: python -m pytest -v"""
import asyncio

import pytest

from starter import ClassificationError, classify_document, make_client


async def classify_with(doc_id: str, api_key: str = "test-key") -> str:
    async with make_client(api_key) as client:
        return await classify_document(client, doc_id)


def test_returns_label() -> None:
    assert asyncio.run(classify_with("DOC-002")) == "contract"


def test_unavailable_service_raises_classification_error() -> None:
    with pytest.raises(ClassificationError, match="DOC-005: HTTP 503"):
        asyncio.run(classify_with("DOC-005"))


def test_wrong_api_key_raises_classification_error() -> None:
    with pytest.raises(ClassificationError, match="HTTP 401"):
        asyncio.run(classify_with("DOC-001", api_key="wrong-key"))
