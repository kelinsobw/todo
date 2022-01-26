import pytest

from django.test import Client

from notes.models import Note


@pytest.mark.django_db
class TestNotes:
    def test_notes_index_view(self):
        client = Client()
        response = client.get("/")
        assert response.status_code == 200

    def test_notes_add_view(self):
        client = Client()

        response = client.post("/", {"title": "test", "text": "text"})
        assert response.status_code == 200
        assert Note.objects.cout() == 1
