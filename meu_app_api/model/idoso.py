from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base, Comentario


class Idoso(Base):
    __tablename__ = 'idoso'

    id = Column("pk_idoso", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    cpf = Column(String(14), unique=True)
    idade = Column(Integer)
    nomeResponsavel = Column(String(140), unique=True)
    numResponsavel = Column(String(13), unique=True)
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o idoso e o comentário.
    # Essa relação é implicita, não está salva na tabela 'idoso',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    comentarios = relationship("Comentario")

    def __init__(self, nome:str, cpf:str, idade:int, nomeResponsavel:str, numResponsavel:str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Idoso

        Arguments:
            nome: nome do idoso
            cpf: número cpf do idoso
            idade: idade do idoso
            nomeResponsavel: nome do responsável pelo idoso
            numResponsavel: número de contato do responsável pelo idoso
            data_insercao: data de quando o idoso foi inserido à base
        """
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.nomeResponsavel = nomeResponsavel
        self.numResponsavel = numResponsavel

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

    def adiciona_comentario(self, comentario:Comentario):
        """ Adiciona um novo comentário ao Idoso
        """
        self.comentarios.append(comentario)

