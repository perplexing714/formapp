from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('question.html')
    
@app.route("/home")
def render_home(): 
    user = request.args['uname']
    reply1 = "Welcome, " + user + "!"
    return render_template('home.html', response1 = reply1)
    
    
@app.route("/verif")
def render_verif(): 
    return render_template('verify.html')
    
if __name__=="__main__":
    app.run(debug=True)
