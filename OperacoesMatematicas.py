import math
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/somar/<int:n1>/<int:n2>')
def somar(n1, n2):
    resultado = n1 + n2
    resultado = str(resultado)
    return jsonify({'resultado':resultado})

@app.route('/subtrair/<int:n1>/<int:n2>')
def subtrair(n1, n2):
    resultado = n1 - n2
    resultado = str(resultado)
    return jsonify({'resultado':resultado})

@app.route('/multiplicar/<int:n1>/<int:n2>')
def multiplicar(n1, n2):
    resultado = n1 * n2
    resultado = str(resultado)
    return jsonify({'resultado':resultado})

@app.route('/multiplicar/<int:n1>/<int:n2>')
def dividir(n1, n2):
    resultado = n1 / n2
    resultado = str(resultado)
    return jsonify({'resultado':resultado})

@app.route('/restodivisao/<int:n1>/<int:n2>')
def restodivisao(n1, n2):
    resultado = n1 % n2
    resultado = str(resultado)
    return jsonify({'resultado':resultado})

@app.route('/exponen/<int:n1>/<int:n2>')
def exponen(n1, n2):
    resultado = n1 ** n2
    resultado = str(resultado)
    return jsonify({'resultado':resultado})

@app.route('/raizquadrada/<int:n1>')
def raizquadrada(n1):
    resultado = math.isqrt(n1)
    resultado = str(resultado)
    return jsonify({'resultado':resultado})

@app.route('/primo/<int:n1>')
def primo(n1):
    n = n1
    mult = 0
    for count in range(2, n):
        if n % count == 0:
            mult += 1
    if mult == 0:
        resultado = 'É primo'
    else:
        resultado = 'Não é primo'
    return jsonify({'resultado': resultado})


app.run()