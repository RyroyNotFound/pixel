from flask import Flask, request
app = Flask(__name__)

tab = [] #Cette liste contiendra ma map en 2D
for i in range():
    tab.append([0] * 6) #Ajoute 30 colonnes de 30 entiers(int) ayant pour valeurs 0

@app.route('/place', methods=['POST'])
def dessin_case():
        return ''

@app.route('/full', methods=['GET'])
def retourne_tableau():
        print(f"OK Get !")
        return ''

print(tab)
app.run()
