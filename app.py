from flask import Flask

app = Flask(__name__)

@app.route('/')
def main_page():
    ''' Main page of site
    '''
    return 'Hello'
