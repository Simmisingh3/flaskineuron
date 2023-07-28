### Create a simple flask application

from flask import Flask, render_template, request, redirect, url_for

## create the flask app

app=Flask(__name__)

@app.route('/')   # decorators used for creating url using .route. Here / means home of a webpage
def home():
    return "<h2>Hello, World!</h2>"

@app.route('/welcome')
def welcome():
    return "Welcome to the flask tutorial"

@app.route('/index')
def index():
    return render_template('index.html')  #render_template folder wants all ur index.html file in the tamplates folder
#redirect used for redirecting a url into webpage

@app.route('/success/<int:score>')   #/success=url, <int:score>=parameter
def success(score):
        return "the person is pass and the score is " + str(score)
    
@app.route('/fail/<int:score>')   #/success=url, <int:score>=parameter example= http://127.0.0.1:5000/success/37
def fail(score):
        return "the person is fail and the score is " + str(score)
#POST = means posting a data and based on that we are getting an info. ex- search a name, search krish, search pwskills
#GET= means getting a website, like looking for google, login in linkedin
@app.route('/calculate', methods=['POST', 'GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        
        average_marks=(maths+science+history)/3
        result= ""
        if average_marks>=50:
            result = "success"
        else:
            result = "fail"
            
        #return redirect(url_for(result, score=average_marks))
    
        return render_template('result.html', results=average_marks)


if __name__ =="__main__": # entry point of code-inside which i will run the app
    app.run(debug=True)
    
