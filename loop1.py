from flask import Flask, render_template, request, jsonify

dict1 = Flask(__name__)

@dict1.route('/')
def home():
    return "<h1>Welcome to the home page</h1>"

@dict1.route('/welcome')
def welcome():
    return "<h1>Welcome to the dictionary page</h1>"

@dict1.route('/index')
def index():
    return render_template('index.html')

@dict1.route('/looping', methods=['GET'])
def looping():
    operation=request.json['operation']
    dictionary1=request.json['dictionary1']
    list1=request.json['list1']
    list2=request.json['list2']
    l = []
    if operation=="loop_of_dictionary":
        for i in dictionary1.items():
            l.append(i)
        result = l
    elif operation=="loop_of_list1":
        for i in list1:
            l.append(i)
        result = l
    elif operation=="loop_of_list2":
        for i in list2:
            l.append(i)
        result = l 
    return "The operation is {} and the result is {}".format(operation, result)



if __name__ == "__main__":
    dict1.run(debug=True)