# flask --app app.py run'''
from flask import Flask

app = Flask(__name__) # create a WSGI application

tarefas = []
concluidas = []

# create the first route
@app.route('/')
def hello_world():
    return 'Hello World!'

# simple routes
@app.route('/tarefas')
def mostrar_tarfas():
    return str(tarefas) #tarefas

@app.route('/concluidas')
def mostrar_concluidas():
    return str(concluidas) #tarefas

# routes with parameters
@app.route('/<name>')
def hello_name(name):
    return f"Hello, {name}"

@app.route('/adicionar/<tarefa>')
def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)
    return 'Tarefa Adicionada'

@app.route('/remover/<tarefa>')
def remover_tarefa(tarefa):
    tarefas.remove(tarefa)
    return 'Tarefa Removida'

@app.route('/concluir/<tarefa>')
def concluir_tarefa(tarefa):
    tarefas.remove(tarefa)
    concluidas.append(tarefa)
    return 'Tarefa Concluída'

# controle de erros (if...else...)
# utilização de arquivos (pandas)