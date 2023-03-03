from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    with open('content.txt', 'r') as f:
        content = f.read()
    return str(content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)