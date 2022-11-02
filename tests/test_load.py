import uuid
import pytest
from dundie.core import load
from .constants import PEOPLE_FILE


def setup_module():
    print("roda antes dos testes desse modulo")


def teardown_module():
    print("roda apos dos testes desse modulo")



@pytest.fixture(scope="function", autouse=True)
def create_new_file(tmpdir):
    file_ = tmpdir.join('new_file.txt')
    file_.write("isso é sujeira")
    yield
    file_.remove()

@pytest.mark.unit
@pytest.mark.high
def test_load(request):
    """Test load function"""
    
    request.addfinalizer(lambda: print("Terminou"))
    
    with open(f"arquivo_indesejado-{uuid.uuid4()}.txt", "w") as file_:
        file_.write("Dados uteis somente para o teste.")
    
    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == 'J'