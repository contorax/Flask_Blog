from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Walter White',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'September  10, 2018'
    },
    {
        'author': 'Zafar Tagiyev',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'February 9, 2019'

    }
    ]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
