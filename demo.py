from flask import Flask, render_template, request
import model
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html', message = 'Aloha, Aloha')
    else:
        username  = request.form['usename']
        password  = request.form['password']
        db_password = model.check_pw(username)
        
        
        if password == db_password:
            message = model.show_color(username)
            return render_template('football.html',message = message)
        else:
            error_message = 'Hint: He curses a lot'
            return render_template('index.html', message = error_message)
        
@app.route('/football', methods = ['GET'])
def football():
    return render_template('football.html')

if __name__ == '__main__':
    app.run(port = 7000, debug = True)
    
