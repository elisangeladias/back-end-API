# API para cadastro de idosos em clínica de repouso

Este pequeno projeto faz parte da avaliação didática da Disciplina **Desenvolvimento Full Stack Básico**, foram aplicados os conhecimentos adquiridos em aula. Para isso foi criado um back-end de cadastro de idosos. Basta baixar o projeto em seu computador, abrir no VSCode e executar os comandos abaixo no terminal da ferramenta para executar esta aplicação. 

---
## Como executar 

Será necessário o Python 3 e ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

1º python3 -m venv env (Para criar o ambiente virtual)
2º acessa o diretório /env (Para acessar o ambiente virtual)
3º Scripts\activate (Para ativar o ambiente virtual)
4º volta um nível, ou seja, saí do diretório /env
5º entra no diretório meu_app_api
5º (env) pip install -r requirements.txt (para instalar dependências/bibliotecas, descritas no arquivo `requirements.txt`)
6º (env) flask run --host 0.0.0.0 --port 5000 (para executar a API )

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env) flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
