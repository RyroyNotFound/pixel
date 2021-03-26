from flask import Flask, request, jsonify
app = Flask(__name__)

tab = [] 
for i in range(30):
    tab.append([0] * 30)

@app.route('/place', methods=['POST'])
def dessin_case():
    x = request.json["x"]
    y = request.json["y"]
    couleur = request.json["color"]
    print(f"X : {x} - Y : {y} - Couleur : {couleur}")
    tab[x][y] = couleur
    print(f"Couleur : {tab[x][y]}")

    return ''

@app.route('/full', methods=['GET'])
def retourne_tableau():
    print(tab)
    return jsonify(tab)

app.run()
