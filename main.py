from flask import Flask, render_template, request
from happytransformer import HappyGeneration

app = Flask(__name__)

def strip_text(text):
    start_index = text.find("\n\nA:\n\n")
    if start_index != -1:
        end_index = text.find("\n", start_index+len("\n\nA:\n\n"))
        if end_index != -1:
            return text[:end_index]
    return text


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gen', methods=['POST'])
def gen():
    input_text = request.data.decode('utf-8') # Decode the input data from bytes to a string
    happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-125M")
    result = happy_gen.generate_text(input_text)
    result = strip_text(result[1])
    return result


app.run('0.0.0.0', port=80)
