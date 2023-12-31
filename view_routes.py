from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
import querys, crud_routes
from main import app

#####################
####### ROTAS #######
#####################
@app.route('/')
def mainpage():
    return render_template('login.html', title='Enter with your credentials')


@app.route('/list')
def listar():
    if 'current_user' not in session or session['current_user'] == None:
        return render_template('login.html', title='Enter with your credentials')

    games = querys.games_query()
    return render_template('list.html', title='My new title', jogos=games)


@app.route('/insert')
def insert():
    if 'current_user' not in session or session['current_user'] == None:
        return render_template('login.html', title='Enter with your credentials')
    
    form = crud_routes.FormJogo()
    return render_template('insert.html', title='Insert a new game', form=form)


@app.post('/auth')
def authenticate():
    users = querys.users_query(request.form['username'])
    
    if len(users) == 0:
        flash('Nome de usuário e/ou senha não encontrado(s). Tente novamente.')
    else:

        if users[0]['password'] == request.form['user_password']:
            session['current_user'] = users[0]['nickname']
            return redirect(url_for('insert'))
            
            #return render_template(url_for('listar'))  # not working idkw
        else:
            flash('Nome de usuário e/ou senha não encontrado(s). Tente novamente.')
    
    return render_template('login.html', title='Enter with your credentials')
    

@app.route('/logout')
def logout():
    session['current_user'] = None
    flash(f"Usuário deslogado.")
    return redirect(url_for("mainpage"))


@app.route('/edit/<id>')
def edit(id):
    if 'current_user' not in session or session['current_user'] == None:
        return render_template('login.html', title='Enter with your credentials')
    
    game_info = querys.games_info(id)
    capa_jogo = crud_routes.get_image(id)

    return render_template('edit.html', title='Edit game', name=game_info[0]['name'], category=game_info[0]['category'], platform=game_info[0]['platform'], game_id=id, capa_jogo=capa_jogo)


@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)