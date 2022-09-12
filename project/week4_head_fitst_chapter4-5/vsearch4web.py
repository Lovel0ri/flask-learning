# @Time: 2022/9/12 1:27
# @Author: 李树斌
# @File : vsearch4web.py
# @Software :PyCharm

from flask import Flask,render_template,request,escape


from vsearch import search4letters

app = Flask(__name__)
def log_request(req:'flask_request',res:str) ->None:
    with open('vsearch.log','a') as log:
        print(req,res,file=log)

@app.route('/search4',methods = ['POST','GET'])
def do_search()-> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are the results'
    results = str(search4letters(phrase,letters))
    log_request(request,results)
    return render_template('results.html',the_phrase = phrase,
                                        the_letters = letters,
                                        the_tilte = title,
                                        the_results = results)

@app.route('/viewlog')
def view_the_log()->str:
    with open('vsearch.log') as log:
        contents = log.read()
    return escape(contents)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',the_title = 'Welcome to search4letters on the web!')


if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)
