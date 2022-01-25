from flask import Flask, render_template
from grayscale import *

app = Flask(__name__)



@app.route("/<filename>")
def hello_world(filename):
    img = get_pillow_img(filename)
    img = img2greyscale(img)
    greyscale_data = list(img.getdata())
    brainfuck = {
        0:'>',
        1: '<',
        2: '+',
        3: '-',
        4: '.',
        5: ',',
        6: '[',
        7: ']'
    }
    brainfucked_data = [brainfuck[val % 8] for val in greyscale_data]
    html_string = html_from_brainfucked_data(brainfucked_data, img.size)

    return f"""
        <span style="font-family: monospace;">{html_string}</span>
    """

if __name__ == '__main__':
    app.run(debug=True)