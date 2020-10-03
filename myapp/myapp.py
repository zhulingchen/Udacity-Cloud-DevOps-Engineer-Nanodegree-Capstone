# reference:
# https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello World!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80