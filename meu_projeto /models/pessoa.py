from models.enums.sexo import Sexo
from models.endereco import Endereco

class Pessoa:
    def __init__(self, id: int, nome: str, DataNascimento: str, telefone: str, email: str, sexo: Sexo, endereco: Endereco) -> None:
        self.id = id
        self.nome = nome
        self.DataNascimento = DataNascimento
        self.telefone = telefone
        self.email = email
        self.sexo = sexo
        self.endereco = endereco

    def __str__(self) -> str:
        return ("===== Dados do Usuário ====="
            f"\nID: {self.id}"
            f"\nNome: {self.nome}"
            f"\nData de nascimento: {self.DataNascimento}"
            f"\nTelefone: {self.telefone}"
            f"\nEmail: {self.email}"
            f"\nSexo: {self.sexo.value} \n"
            f"\n===== Endereço do Usuário ====="
            f"\Endereço: {self.endereco}"
        )