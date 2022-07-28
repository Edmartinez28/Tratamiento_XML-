from flask import Flask, render_template, request, redirect, url_for , jsonify , make_response
import pickle
import os


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

vectorizerSVM = pickle.load(open('Modelos_IA/Modelo del SVM/vectorizer.sav', 'rb'))
classifierSVM = pickle.load(open('Modelos_IA/Modelo del SVM/classifierSVM.sav', 'rb'))

modelKNN = pickle.load(open('Modelos_IA/Modelo del KNN/knn_model.sav', 'rb'))

vectorNaiveBayes= pickle.load(open('Modelos_IA/Modelo de Naive Bayes/count_vector.sav', 'rb'))
modeloNaiveBayes = pickle.load(open('Modelos_IA/Modelo de Naive Bayes/naive_bayes.sav', 'rb'))

def sentiment_analysis_SVM(text):
    if text:
        text_vector = vectorizerSVM.transform([text])
        result = classifierSVM.predict(text_vector)
        print(result)
        return result[0]
    return make_response(jsonify({'error':'sorry! unable to parse', 'status_code':500}), 500)

@app.route('/')
def hello_world():  # put application's code here
    return render_template('mensaje.html')


@app.route('/definir', methods=['POST'])
def determinar_emocion():
    if request.method == 'POST':
        mens = request.form['mensaje']
        sentimentResult = sentiment_analysis_SVM(mens)
        return render_template('sentimiento.html',mensajecont=mens , svm=sentimentResult)

if __name__ == '__main__':
    app.run(port=5000, debug=True)

@app.route('/sentimiento' , methods=['POST'])
def devolver_mensaje():
    if request.method == 'POST':
        return render_template('mensaje.html')