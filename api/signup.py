from app import app


@app.route('/signup')
def hello_world():
    return 'Hello World!'
