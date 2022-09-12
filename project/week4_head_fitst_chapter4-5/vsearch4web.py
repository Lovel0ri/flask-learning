# @Time: 2022/9/12 1:27
# @Author: 李树斌
# @File : vsearch4web.py
# @Software :PyCharm

from flask import Flask,render_template,request,escape

from vsearch import search4letters

app = Flask(__name__)

"""写入记录日志文件"""
def log_request(req:'flask_request',res:str) ->None:
    with open('vsearch.log','a') as log:
        """从web应用的html表单提交的数据，运行web浏览器的ip地址，提交数据的浏览器的标识"""
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


@app.route('/search4',methods = ['POST','GET'])
def do_search()-> 'html':
    title = 'Here are the results'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase,letters))
    log_request(request,results)
    return render_template('results.html',the_phrase = phrase,
                                        the_letters = letters,
                                        the_tilte = title,
                                        the_results = results)

@app.route('/viewlog')
def view_the_log()->'html':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    return  str(contents)

    titles = ['Form Data','Remote_addr','User_agent','Results']
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)
    # return escape(''.join(contents))


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',the_title = 'Welcome to search4letters on the web!')


if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)
