from flask import Flask
import easyocr
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/ocr')
def ocr():
    reader = easyocr.Reader(['en'])  # this needs to run only once to load the model into memory
    result = reader.readtext('card.png')
    return {"message": result}

if __name__ == '__main__':
    app.run()
