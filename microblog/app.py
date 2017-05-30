from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def index(name='Anonymous'):
    return render_template('index.html', name=name)


@app.route('/add', methods=['GET', 'POST'])
def add():
    name = post = ''
    if request.method == 'POST':
        post = request.form.get('post', '')
        name = request.form.get('name', '')
        if post and name:
            return redirect('/')
    return render_template('add.html', name=name, post=post)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
