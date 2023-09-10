from flask import jsonify, render_template
from flask import Flask
import flask_cors

app = Flask(__name__)
flask_cors.CORS(app)

def generate_pswd_fibr(ssid: str):
    char_to_hex = {
        '0': 'f', '1': 'e', '2': 'd', '3': 'c',
        '4': 'b', '5': 'a', '6': '9', '7': '8',
        '8': '7', '9': '6', 'a': '5', 'b': '4',
        'c': '3', 'd': '2', 'e': '1', 'f': '0',
        'A': 'F', 'B': 'E', 'C': 'D', 'D': 'C',
        'E': 'B', 'F': 'A', 'G': '9', 'H': '8',
        'I': '7', 'J': '6', 'K': '5', 'L': '4',
        'M': '3', 'N': '2', 'O': '1', 'P': '0',
        'Q': 'F', 'R': 'E', 'S': 'D', 'T': 'C',
        'U': 'B', 'V': 'A', 'W': '9', 'X': '8',
        'Y': '7', 'Z': '6'
    }
    calculated_mac = ""
    for char in ssid:
        if char in char_to_hex:
            calculated_mac += char_to_hex[char]
        else:
            calculated_mac += char

    return "PLDTWIFI" + calculated_mac.upper()


def generate_pswd_dsl(digit):
    digit = int(digit)
    pswd = digit * 3
    return f"PLDTWIFI{pswd}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fibr/<ssid>', methods=['GET'])
def pldt_fibr(ssid: str):
    return jsonify({'ssid' : ssid,'password': generate_pswd_fibr(ssid[-5:])})

@app.route('/dsl/<ssid>', methods=['GET'])
def pldt_dsl(ssid: str):
    return jsonify({'ssid' : ssid,'password': generate_pswd_dsl(ssid[-5:])})

if __name__ == '__main__':
    app.run(debug=True)
