import pytest
from src.model.repositories.subscribers_repository import SubscribersRepository

@pytest.mark.skip("Teste insert Subscriber in DB")
def test_insert_subscriber():
    subscriber_infos = {
        'nome': 'teste nome2123',
        'email': 'teste emai2l12',
        'evento_id': 1
    }

    subscriber_repo = SubscribersRepository()
    subscriber_repo.insert(subscriber_infos)

@pytest.mark.skip("Teste select Subscriber s in DB")

def test_select_subscriber():
    email = 'teste email'
    evento_id = 2

    subscriber_repo = SubscribersRepository()

    event = subscriber_repo.select_subscriber(email, evento_id)

    print(event.email)
    print(event.nome)
    print(event.evento_id)

