from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
<<<<<<< HEAD
    return "Hello World! From Maurizio Lupini, Updated : ) v1"
=======
    return "Hello World! From Maurizio Lupini, Updated : )"
>>>>>>> 71f5e18246b3263d1039efc993c093f602cf0843

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
