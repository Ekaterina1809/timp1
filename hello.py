from flask import Flask, render_template, request, abort
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Hello.html')

@app.route('/user/<name>')
@app.route('/user/')
def user(name=None):
    if name is None:
        name=request.args.get('name')
    if name:
        return render_template('Hello.html', name=name)
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
