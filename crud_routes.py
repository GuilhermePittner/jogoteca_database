from wtforms import StringField, validators, SubmitField
from flask import request, redirect, flash, url_for
from flask_wtf import FlaskForm
import querys, os, time
from main import app


#===================#
#      WTFORMS      #
#===================#
class FormJogo(FlaskForm):
    name = StringField('Nome do Jogo', [validators.DataRequired(), validators.Length(min=1, max=30)])
    category = StringField('Categoria do Jogo', [validators.DataRequired(), validators.Length(min=1, max=30)])
    console = StringField('Console', [validators.DataRequired(), validators.Length(min=1, max=30)])

    submit = SubmitField('Salvar')


#===================#
#       GAME        #
#===================#
#@app.route('/new_game', methods=['POST',])
@app.post('/new_game')
def new_game():
    form = FormJogo(request.form)

    if not form.validate_on_submit():
        return redirect(url_for('insert'))
    
    
    nome = form.name.data
    categoria = form.category.data
    console = form.console.data
    

    game_check = querys.check_games(nome)
    if game_check:
        flash('Jogo já existente!')
    else:
        id = querys.insert_games(nome, categoria, console)
        flash('Jogo inserido!')

        print(f'segue id {id}')

        timestamp = time.time()
        file = request.files['file']
        file.save(f'uploads/capa_{id}-{timestamp}.jpg')
        
    #novoJogo = classes.meusJogos(nome, categoria, console)
    #classes.games.append(novoJogo)

    return redirect("/list")


@app.post('/edit_game')
def edit_game():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    id = request.form['game_id']

    delete_image(id)

    timestamp = time.time()
    file = request.files['file']
    file.save(f'uploads/capa_{id}-{timestamp}.jpg')
    
    querys.update_games(nome, categoria, console, id)

    return redirect("/list")


@app.route('/delete/<id>')
def delete(id):
    querys.delete_games(id)
    delete_image(id)
    return redirect("/list")



#===================#
#       IMAGE       #
#===================#
def get_image(id):
    for file_name in os.listdir('uploads/'):
        if f'capa_{id}' in file_name:
            return file_name
        
    return 'capa_random.jpg'


def delete_image(id):
    filename = get_image(id)
    if filename != 'capa_random.jpg':
        os.remove(f'uploads/{filename}')