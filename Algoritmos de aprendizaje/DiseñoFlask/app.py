from flask import Flask, render_template, request, redirect, url_for , jsonify , make_response
import pickle
import os


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

vectorizer = pickle.load(open('Modelos_IA/Modelo del SVM/vectorizer.sav', 'rb'))
classifier = pickle.load(open('Modelos_IA/Modelo del SVM/classifierSVM.sav', 'rb'))

def sentiment_analysis(text):
    if text:
        text_vector = vectorizer.transform([text])
        result = classifier.predict(text_vector)
        print(result)
        return result[0]
    return make_response(jsonify({'error':'sorry! unable to parse', 'status_code':500}), 500)

@app.route('/')
def hello_world():  # put application's code here
    print("Se fue a Hola Mundo 2")
    return render_template('mensaje.html')

@app.route('/positivo')
def colocar_positivo():
    return render_template('positivo.html')


@app.route('/negativo')
def colocar_negativo():
    return render_template('negativo.html')


@app.route('/neutro')
def colocar_neutro():
    return render_template('neutro.html')

@app.route('/none')
def colocar_none():
    return render_template('none.html')

@app.route('/positivo' , methods=['POST'])
def devolver_positivo():
    if request.method == 'POST':
        return render_template('mensaje.html')

@app.route('/negativo' , methods=['POST'])
def devolver_negtivo():
    if request.method == 'POST':
        return render_template('mensaje.html')

@app.route('/neutro' , methods=['POST'])
def devolver_neutro():
    if request.method == 'POST':
        return render_template('mensaje.html')

@app.route('/none' , methods=['POST'])
def devolver_none():
    if request.method == 'POST':
        return render_template('mensaje.html')

@app.route('/definir', methods=['POST'])
def determinar_emocion():
    if request.method == 'POST':
        mens = request.form['mensaje']
        print(mens)

        analisis = sentiment_analysis(mens)
        if analisis == 'P':
            return redirect(url_for('colocar_positivo'))
        elif analisis == 'N':
            return redirect(url_for('colocar_negativo'))
        elif analisis == 'NEU':
            return redirect(url_for('colocar_negativo'))
        else:
            return redirect(url_for('colocar_none'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)

@app.route('/sentimiento/<mensajecont>')
def colocar_none(mensajecont):
    return render_template('none.html' , mensajecont=mensajecont)

@app.route('/positivo' , methods=['POST'])
def devolver_positivo():
    if request.method == 'POST':
        return render_template('mensaje.html')