from flask import Flask, request
app = Flask(__name__)

COLORS = [
    (255, 255, 255), # White
    (0, 0, 0), # Black
    (255, 0, 0), # Red
    (51, 204, 51), # Green
    (0, 153, 255), # Blue
    (255, 51, 204), # Pink
    (255, 153, 0), # Orange
    (255, 255, 0), # Yellow
    (153, 0, 204), # Purple
    (128, 128, 128), # Gray
]

tab = [] #Cette liste contiendra ma map en 2D
for i in range():
    tab.append([0] * 6) #Ajoute 30 colonnes de 30 entiers(int) ayant pour valeurs 0

@app.route('/place', methods=['POST'])
def dessin_case():
        return ''

@app.route('/full', methods=['GET'])
def retourne_tableau():
        print(f"OK Get !")
        return tab

print(tab)
app.run()
