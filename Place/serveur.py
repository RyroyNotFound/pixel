from flask import Flask, request
app = Flask(__name__)


@app.route('/hello', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        nom = request.json['name']
        print(f"Envoi de la requete post pour \"{nom}\"")
        return nom
    else :
        print(f"Envoi de la requete get pour \"Jim\"")
        return 'Bonjour Jim ! (GET)'



app.run()
