from flask import Flask

app = Flask(__name__)

greetings = {
    'english': 'Hello!', 
    'maori': 'Kia Ora!', 
    'dutch': 'Hallo!', 
    'french': 'Bonjour!'    
}

unsupported_language_message = 'Sorry! I don\'t know that language'

@app.route('/', methods=['GET'])
def default():
    return 'Depop Interview Demo!'

@app.route('/greet', methods=['GET'])
@app.route('/greet/<language>', methods=['GET'])
def greet(language = 'maori'):
    language_key = language.lower()
    return greetings.get(language_key, unsupported_language_message)