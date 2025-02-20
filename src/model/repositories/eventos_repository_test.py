import pytest
from src.model.repositories.eventos_repository import EventosRepository

@pytest.mark.skip("Teste de insert")
def test_insert_eventos():
    event_name = "Test Evento 2"
    event_repo = EventosRepository()

    event_repo.insert(event_name)

@pytest.mark.skip("Teste de select")
def test_select_event():
    event_name = "Test Evento 2"
    event_repo = EventosRepository()

    event = event_repo.select_event(event_name)
    print(event)
    print(event.nome)