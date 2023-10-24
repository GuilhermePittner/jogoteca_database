from flask import Flask, render_template, request, redirect, session, flash, url_for
import querys


app = Flask(__name__)
app.secret_key = 'tribo'


from view_routes import *
from crud_routes import *
if __name__ == '__main__':
    app.run(debug=True)