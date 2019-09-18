from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'first_name': 'Jeffrey',
        'last_name': 'Tram',
    },
    {
        'first_name': 'Bradford',
        'last_name': 'Peterson'
    },
    {
        'first_name': 'Robert',
        'last_name': 'Giuffreda'
    }
]

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title='About', posts=posts)


if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 80, debug = True)