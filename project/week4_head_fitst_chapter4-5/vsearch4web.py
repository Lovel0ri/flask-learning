# @Time: 2022/9/12 1:27
# @Author: 李树斌
# @File : vsearch4web.py
# @Software :PyCharm
# import vsearch
from flask import Flask,render_template,request
from dist.vsearch import search4letters
app = Flask(__name__)


@app.route('/')
def hello()->str:  # put application's code here
    return 'Hello World from Flask'

@app.route('/search4',methods = ['POST'])
def do_search()-> str:
    return str(search4letters('life,the universe,and everything','aeiou,!'))
    phrase = request.form['phrase']
    letters = request.form['letters']
    return str(search4letters(phrase,letters))
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title = 'Welcome to search4letters on the web!')


# if __name__ == '__main__':
app.run(debug=True, host="127.0.0.1", port=5000)
