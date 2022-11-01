from flask import Flask, render_template, request


def get_users():
    return ['mike', 'mishel', 'adel', 'keks', 'kamila']


app = Flask(__name__)


@app.route('/users/')
def users():
    users = get_users()
    term = request.args.get('term')
    filtered_courses = filter(lambda x: term in x, users)
    return render_template(
        'users/index.html',
        users=filtered_courses,
        search=term,
    )


app.run()
