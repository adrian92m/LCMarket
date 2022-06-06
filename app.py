from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "This is the place, where new service will be created. Please wait patiently!!!!!!!"

if __name__ == "__main__":
    app.run()
