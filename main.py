from flask import Flask, render_template, request
import random

app = Flask(__name__)

dice_faces = {
    1: '&#9856;',  # ⚀
    2: '&#9857;',  # ⚁
    3: '&#9858;',  # ⚂
    4: '&#9859;',  # ⚃
    5: '&#9860;',  # ⚄
    6: '&#9861;',  # ⚅
}

@app.route('/', methods=['GET', 'POST'])
def dice_simulator():
    dice_value = None
    if request.method == 'POST':
        dice_value = random.randint(1, 6)
    return render_template('index.html',  dice_value=dice_faces.get(dice_value))

if __name__ == '__main__':
    app.run(debug=True)
