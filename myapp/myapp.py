# reference:
# https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    browser_str = "<h1 style='color:blue'>Hello World!<br>" \
                  "This is Lingchen Zhu's Udacity Cloud DevOps Engineer Capstone Project.<br>" \
                  "Built on Flask and Gunicorn</h1>"
    return browser_str

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80