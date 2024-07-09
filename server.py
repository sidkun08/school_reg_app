from flask import Flask, render_template, request
from School import register, search, json_list
from student import Student
import json

app = Flask(__name__)

@app.route('/')
def web_app():
    return render_template(template_name_or_list='main.html')

@app.route('/submit_registration')
def main_check():
    action = request.args.get("action")
    print(action)
    if action == "register":
        return render_template(template_name_or_list='reg_application.html')
    elif action == "search":
        return render_template(template_name_or_list='search_verify.html')
    elif action == "leave":
        return render_template(template_name_or_list='leave.html')
    else:
        return render_template(template_name_or_list='main.html')

@app.route("/main.html")
def redirect():
    return render_template(template_name_or_list='main.html')

@app.route("/registration_submit")
def reg_form():
    fname = request.values.get("fname")
    lname = request.values.get("lname")
    grade = request.values.get("grade")
    gender = request.values.get("gender")
    height = request.values.get("height")
    address = request.values.get("address")
    major = request.values.get("major")

    student = Student(fname, lname, grade, gender, height, address, major)
    with open('data.json') as jsonfile:
        json_list = json.load(jsonfile)
    
    json_list.append(student.__dict__)

    with open('data.json', 'w') as jsonfile:
        json.dump(json_list, jsonfile, indent=4, separators=(",", ": "))
    
    return render_template(template_name_or_list='confirmation.html')

@app.route("/search_type")
def search_verify():
    action = request.args.get("action")
    if action == "public":
        return render_template(template_name_or_list="pub_search_application.html")
    elif action == "private":
        return render_template(template_name_or_list="login_signup.html")
    else:
        return render_template(template_name_or_list="search_verify.html")
    
@app.route("/public_search_submit")
def public_search():
    check = False
    fname = request.values.get("fname")
    lname = request.values.get("lname")
    grade = request.values.get("grade")
    major = request.values.get("major")

    with open('data.json', 'r') as jsonfile:
        data = json.load(jsonfile)
        for i in data:
            if i.get("fname") == fname:
                if i.get("lname") == lname:
                    if i.get("grade") == grade:
                        if i.get("interest") == major:
                            check = True
                        else:
                            check=False
    if check == True:
        search_student = Student(fname, lname, grade, None, None, None, major)
        return search_student.getPublic()
    else:
        return "Could not locate Student. Try Again Later"

@app.route("/login_signup")
def login_signup():
    action = request.args.get("action")
    print(action)
    if action == "sign_up":
        return render_template(template_name_or_list="sign_up.html")
    elif action == "login":
        return render_template(template_name_or_list="login.html")
    else:
        return render_template(template_name_or_list="login_signup.html")


@app.route("/sign_up")
def sign_up():
    username = request.values.get("username")
    password = request.values.get("password")

    with open('user.json') as user_data:
        json_list = json.load(user_data)
    
    json_list.append({"username" : username, "password" : password})

    with open('user.json', 'w') as user_data:
        json.dump(json_list, user_data, indent=4, separators=(",", ": "))
    
    return render_template(template_name_or_list="login.html")

@app.route("/login")
def login():
    username = request.values.get("username")
    password = request.values.get("password")
    indicator = False
    with open('user.json', 'r') as user_data:
        user = json.load(user_data)
        for i in user:
            if i.get("username") == username:
                if i.get("password") == password:
                    indicator = True
    if indicator == True:
        return render_template(template_name_or_list="pri_search_application.html")
    else:
        return render_template(template_name_or_list="login_signup.html")
    
@app.route("/private_search_submit")
def private_search():
    check = False
    fname = request.values.get("fname")
    lname = request.values.get("lname")
    grade = request.values.get("grade")
    major = request.values.get("major")

    with open('data.json', 'r') as jsonfile:
        data = json.load(jsonfile)
        for i in data:
            if i.get("fname") == fname:
                if i.get("lname") == lname:
                    if i.get("grade") == grade:
                        if i.get("interest") == major:
                            check = True
                            search_student = Student(fname, lname, grade, i.get("gender"), i.get("height"), i.get("_address"), major)
                        else:
                            check=False
    if check == True:
        return search_student.getPrivate()
    else:
        return "Could not locate Student. Try Again Later"
                



if __name__ == "__main__":
    app.run()