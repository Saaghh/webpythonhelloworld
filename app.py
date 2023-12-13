from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hello():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello, World!</title>
    </head>
    <body>
        <h1>Привет Лолочка, Котеночек милая бусинка <3</h1>
    </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)