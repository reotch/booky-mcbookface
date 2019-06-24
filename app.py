from flask import Flask, render_template, request
from flask_cors import CORS
from models import create_post, get_posts

app = Flask(__name__)

CORS(app)

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_post(name, post)

    if request.method == 'GET':
        pass

    posts = get_posts()
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)