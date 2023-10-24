from flask import render_template, request, redirect, session, flash, url_for
from main import app
import querys

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
    
    return render_template('insert.html', title='Insert a new game')


@app.post('/auth')
def authenticate():
    users = querys.users_query(request.form['username'])
    
    if len(users) == 0:
        flash('Nome de usuário e/ou senha não encontrado(s). Tente novamente.')
    else:

        if users[0]['password'] == request.form['user_password']:
            session['current_user'] = users[0]['nickname']
            return render_template('insert.html', title='Insert a new game')
            
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
    return render_template('edit.html', title='Edit game', name=game_info[0]['name'], category=game_info[0]['category'], platform=game_info[0]['platform'], game_id=id)    