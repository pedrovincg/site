from flask import flask

app= Flaks(__name__)

@app.route('/')
def hello_world()
    return 'Hello World'

if name == 'main':
    app.run()