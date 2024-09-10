import os

from models.enums.UnidadeFederativa import UnidadeFederativa
from models.enums.sexo import Sexo
from models.endereco import Endereco
from models.pessoa import Pessoa

os.system("cls || clear")

#Instanciando classe.
pessoa1 = Pessoa(17759, "Fausto Silva", "25/08/1902", "(89) 98532-0632", 
                 "OlokinhoMeu123@gmail.com", Sexo.MASCULINO, Endereco("Rua das Cassetadas", 1820, 
                    "Próximo aos reclames do PlimPlim", "80520", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO))

print(pessoa1)