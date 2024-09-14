from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Idoso, Comentario
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
idoso_tag = Tag(name="Idoso", description="Adição, visualização e remoção de idosos à base")
comentario_tag = Tag(name="Comentario", description="Adição de um comentário à um idoso cadastrado na base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/idoso', tags=[idoso_tag],
          responses={"200": IdosoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_idoso(form: IdosoSchema):
    """Adiciona um novo Idoso à base de dados

    Retorna uma representação dos idosos e comentários associados.
    """
    idoso = Idoso(
        nome=form.nome,
        cpf=form.cpf,
        idade=form.idade,
        nomeResponsavel=form.nomeResponsavel,
        numResponsavel=form.numResponsavel)
    logger.debug(f"Adicionando idoso de nome: '{idoso.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando idoso
        session.add(idoso)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado idoso de nome: '{idoso.nome}'")
        return apresenta_idoso(idoso), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Idoso de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar idoso '{idoso.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar idoso '{idoso.nome}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/idosos', tags=[idoso_tag],
         responses={"200": ListagemIdososSchema, "404": ErrorSchema})
def get_idosos():
    """Faz a busca por todos os Idosos cadastrados

    Retorna uma representação da listagem de idosos.
    """
    logger.debug(f"Coletando idosos ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    idosos = session.query(Idoso).all()

    if not idosos:
        # se não há idosos cadastrados
        return {"idosos": []}, 200
    else:
        logger.debug(f"%d idosos econtrados" % len(idosos))
        # retorna a representação de idoso
        print(idosos)
        return apresenta_idosos(idosos), 200


@app.get('/idoso', tags=[idoso_tag],
         responses={"200": IdosoViewSchema, "404": ErrorSchema})
def get_idoso(query: IdosoBuscaSchema):
    """Faz a busca por um Idoso a partir do nome do idoso

    Retorna uma representação dos idosos e comentários associados.
    """
    idoso_id = query.id
    logger.debug(f"Coletando dados sobre idoso #{idoso_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    idoso = session.query(Idoso).filter(Idoso.id == idoso_id).first()

    if not idoso:
        # se o idoso não foi encontrado
        error_msg = "Idose não encontrado na base :/"
        logger.warning(f"Erro ao buscar idoso '{idoso_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Idoso econtrado: '{idoso.nome}'")
        # retorna a representação de idoso
        return apresenta_idoso(idoso), 200


@app.delete('/idoso', tags=[idoso_tag],
            responses={"200": IdosoDelSchema, "404": ErrorSchema})
def del_idoso(query: IdosoBuscaSchema):
    """Deleta um Idoso a partir do nome de idoso informado

    Retorna uma mensagem de confirmação da remoção.
    """
    idoso_nome = unquote(unquote(query.nome))
    print(idoso_nome)
    logger.debug(f"Deletando dados sobre idoso #{idoso_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Idoso).filter(Idoso.nome == idoso_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado idoso #{idoso_nome}")
        return {"mesage": "Idoso removido", "id": idoso_nome}
    else:
        # se o idoso não foi encontrado
        error_msg = "Idoso não encontrado na base :/"
        logger.warning(f"Erro ao deletar idoso #'{idoso_nome}', {error_msg}")
        return {"mesage": error_msg}, 404


@app.post('/cometario', tags=[comentario_tag],
          responses={"200": IdosoViewSchema, "404": ErrorSchema})
def add_comentario(form: ComentarioSchema):
    """Adiciona de um novo comentário à um idoso cadastrado na base identificado pelo id

    Retorna uma representação dos idosos e comentários associados.
    """
    idoso_id  = form.idoso_id
    logger.debug(f"Adicionando comentários ao idoso #{idoso_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca pelo idoso
    idoso = session.query(Idoso).filter(Idoso.id == idoso_id).first()

    if not idoso:
        # se idoso não encontrado
        error_msg = "Idoso não encontrado na base :/"
        logger.warning(f"Erro ao adicionar comentário ao idoso '{idoso_id}', {error_msg}")
        return {"mesage": error_msg}, 404

    # criando o comentário
    texto = form.texto
    comentario = Comentario(texto)

    # adicionando o comentário ao idoso
    idoso.adiciona_comentario(comentario)
    session.commit()

    logger.debug(f"Adicionado comentário ao idoso #{idoso_id}")

    # retorna a representação de idoso
    return apresenta_idoso(idoso), 200
