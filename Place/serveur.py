from flask import Flask, request
app = Flask(__name__)

tab = [] 
for i in range(5):
    tab.append([0] * 6)

@app.route('/place', methods=['POST'])
def dessin_case():
    x = request.json["x"]
    y = request.json["y"]
    couleur = request.json["color"]

    return ''

@app.route('/full', methods=['GET'])
def retourne_tableau():
    print(f"Retourne le tableau !")
    return tab

print(tab)
app.run()
