import os

from models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.enums.endereco import Endereco

os.system("cls || clear")

#Instanciando classe.
pessoa1 = Pessoa("Marta", 22, Sexo.FEMININO,
                 Endereco("Rua A", 72))

print(pessoa1)