from flask import Flask
app = Flask(__name__) # Attention : deux underscores avant et après name

@app.route('/')
def home():
    return "Bonjour à tous, Ceci est une simple application conteneurisée avec Docker par Dochrane!"

if __name__ == "__main__": # Attention : deux underscores ici aussi
    app.run(host='0.0.0.0', port=5000)
