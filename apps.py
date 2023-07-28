from flask import Flask, render_template, request, redirect, url_for

## create the flask app

apps=Flask(__name__)

@apps.route('/')   # decorators used for creating url using .route. Here / means home of a webpage
def home():
    return "<h2>Hello, World!</h2>"

@apps.route('/welcome')
def welcome():
    return "Welcome to the flask tutorial"

@apps.route('/index')
def index():
    return render_template('index.html')  #render_template folder wants all ur index.html file in the tamplates folder
#redirect used for redirecting a url into webpage

@apps.route('/success/<int:score>')   #/success=url, <int:score>=parameter,example= http://127.0.0.1:5000/success/37
def success(score):
        return "the person is pass and the score is " + str(score)
    
@apps.route('/fail/<int:score>')  #example= http://127.0.0.1:5000/fail/3
def fail(score):
    return "the person is fail and the score is " + str(score)

@apps.route('/calculate', methods=['POST', 'GET'])
def calculate():
    if request.method=='GET': 
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        
        average_marks=(maths+science+history)/3
        result = ""
        if average_marks >= 50:
            result = "success"
        else:
            result = "fail"
            
        return redirect(url_for(result, score=average_marks))
        #return render_template('result.html', results=average_marks)
        
        
    
if __name__ =="__main__": # entry point of code-inside which i will run the app
    apps.run(debug=True)
    