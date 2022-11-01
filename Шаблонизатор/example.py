from flask import Flask, render_template

app = Flask(__name__)


@app.route('/users/<id>')
def users(id):
    return render_template(
        'users/show.html',
        name=id,
    )


app.run()
