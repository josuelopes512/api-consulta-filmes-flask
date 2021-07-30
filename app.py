from flask import Flask, request, render_template
from googletrans import Translator
from string import capwords
from models import Filme
import requests, os

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pesquisar', methods=['POST'])
def pesquisar():
    try:
        traduzido = tradutor(request.form['pesquisar_filme'], dest='en')
        pesquisa_filme = traduzido.lower().replace(' ', '+')
        URL = 'http://www.omdbapi.com/?t={}&apikey={}'.format(pesquisa_filme, API_KEY)
        result = requests.request('GET', URL)
        result = result.json()
        inexistente = False
    except:
        erro = 'Filme Inexistente'
        inexistente = True
        return render_template('index.html', erro = erro, inexistente = inexistente)
    try:
        nome_filme = capwords(tradutor(result["Title"]))
    except:
        erro = 'Filme Inexistente'
        inexistente = True
        return render_template('index.html', erro = erro, inexistente = inexistente)
    ano = result["Year"]
    classificacao = result["Rated"]
    duracao = result["Runtime"]
    genero = capwords(tradutor(result["Genre"]).replace(', ', ' - ')).replace(' - ', ', ')
    diretor = result['Director']
    elenco = result['Actors']
    resumo = tradutor(result['Plot'])
    poster = result['Poster']

    filme_classe = Filme(nome_filme, ano, classificacao, duracao, genero, diretor, elenco, resumo, poster)

    return render_template('index.html', nome_filme = nome_filme, ano = ano, classificacao = classificacao, duracao = duracao, genero = genero, diretor = diretor, elenco = elenco, resumo = resumo, poster = poster)


def tradutor(palavra, dest='pt'):
    return Translator().translate(palavra, dest=dest).text


if __name__ == '__main__':
    app.run(debug=True)