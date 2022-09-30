from flask import Flask, url_for, redirect, render_template, request
import pandas as pd

app = Flask(__name__) # create a WSGI application

tarefas = pd.read_csv('tarefas.csv', index_col='tarefas')['concluidas']

@app.route('/')
def index():
    if request.args.get('habito') and request.args.get('habito') not in tarefas.index:
        tarefas[request.args.get('habito')] = False
        tarefas.to_csv('tarefas.csv', index_label='tarefas')
    return render_template('app.html', tarefas=tarefas)

@app.route('/remover/<string:tarefa>')
def remover(tarefa):
    del tarefas[tarefa]
    tarefas.to_csv('tarefas.csv', index_label='tarefas')
    print(f'Tarefa {tarefa} removida!')
    return redirect(url_for('index'))

@app.route('/concluir/<string:tarefa>')
def concluir(tarefa):
    tarefas[tarefa] = True
    print(f'Tarefa {tarefa} concluída!')
    return redirect(url_for('index'))

@app.route('/restaurar/<string:tarefa>')
def restaurar(tarefa):
    tarefas[tarefa] = False
    print(f'Tarefa {tarefa} concluída!')
    return redirect(url_for('index'))