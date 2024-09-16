import pytest
from ..models.pessoa import Pessoa # Caminho Relativo.
from ..models.endereco import Endereco # Caminho Absoluto
from ..models.enums.sexo import Sexo 
from ..models.enums.UnidadeFederativa import UnidadeFederativa 

# Modelo.
@pytest.fixture
def criar_pessoa():
    pessoa1 = Pessoa(5546, "Marta", "05/05/2001", "(85) 98562-3532", "dgdfgh", Sexo.FEMININO, 
                    Endereco("Rua das Cassetadas", 1820, 
                    "Próximo aos reclames do PlimPlim", "80520", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO))
    
    return pessoa1

def test_pessoa_atributo_nome(criar_pessoa):
    assert criar_pessoa.nome == "Marta"

def test_pessoa_atributo_idade(criar_pessoa):
    assert criar_pessoa.nome == 22

def test_indereco_logradouro_de_pessoa(criar_pessoa):
    assert criar_pessoa.endereco.logradouro == "Rua. A"