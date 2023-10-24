from flask import request, redirect, flash
from main import app
import querys

#####################
######## CRUD #######
#####################

#@app.route('/new_game', methods=['POST',])
@app.post('/new_game')
def new_game():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    game_check = querys.check_games(nome)
    if game_check:
        flash('Jogo já existente!')
    else:
        querys.insert_games(nome, categoria, console)
        flash('Jogo inserido!')
        
    #novoJogo = classes.meusJogos(nome, categoria, console)
    #classes.games.append(novoJogo)

    return redirect("/list")


@app.post('/edit_game')
def edit_game():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    id = request.form['game_id']

    querys.update_games(nome, categoria, console, id)

    return redirect("/list")


@app.route('/delete/<id>')
def delete(id):
    querys.delete_games(id)
    return redirect("/list")