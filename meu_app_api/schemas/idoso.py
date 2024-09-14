from pydantic import BaseModel
from typing import Optional, List
from model.idoso import Idoso

from schemas import ComentarioSchema


class IdosoSchema(BaseModel):
    """ Define como um novo idoso a ser inserido deve ser representado
    """
    nome: str = "João Silva"
    cpf: str = "030.025.899-26"
    idade: Optional[int] = 92
    nomeResponsavel: str = "João Silva Filho"
    numResponsavel: str = "41 99843-8239"


class IdosoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do idoso.
    """
    nome: str = "Teste"


class ListagemIdososSchema(BaseModel):
    """ Define como uma listagem de idosos será retornada.
    """
    idosos:List[IdosoSchema]


def apresenta_idosos(idosos: List[Idoso]):
    """ Retorna uma representação do idoso seguindo o schema definido em
        IdosoViewSchema.
    """
    result = []
    for idoso in idosos:
        result.append({
            "nome": idoso.nome,
            "cpf": idoso.cpf,
            "idade": idoso.idade,
            "nomeResponsavel": idoso.nomeResponsavel,
            "numResponsavel": idoso.numResponsavel,
        })

    return {"idosos": result}


class IdosoViewSchema(BaseModel):
    """ Define como um idoso será retornado: idoso + comentários.
    """
    id: int = 1
    nome: str = "João Silva"
    cpf: str = "030.025.899-26"
    idade: Optional[int] = 92
    nomeResponsavel: str = "João Silva Filho"
    numResponsavel: str = "41 99843-8239"
    total_cometarios: int = 1
    comentarios:List[ComentarioSchema]


class IdosoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_idoso(idoso: Idoso):
    """ Retorna uma representação do idoso seguindo o schema definido em
        IdosoViewSchema.
    """
    return {
        "id": idoso.id,
        "nome": idoso.nome,
        "cpf": idoso.cpf,
        "idade": idoso.idade,
        "nomeResponsavel": idoso.nomeResponsavel,
        "numResponsavel": idoso.numResponsavel,
        "total_cometarios": len(idoso.comentarios),
        "comentarios": [{"texto": c.texto} for c in idoso.comentarios]
    }
