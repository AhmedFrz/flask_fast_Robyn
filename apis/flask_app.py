from flask import Flask 

# Setup the Flask application
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, this is a flask test'

if __name__ ==  '__main__':
    
    # Run the Flask application
    app.run(host='0.0.0.0', port=8080)

