from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/portfolio')
def portf():
    return render_template('portfolio.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')




if __name__ == '__main__':
    app.run(debug=True)