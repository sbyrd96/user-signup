from flask import Flask, request, redirect, render_template, flash

app = Flask(__name__)
app.config['DEBUG'] = True  

def is_email(string):
    atsign_index = string.find('@')
    atsign_present = atsign_index >= 0
    if not atsign_present:
        return False
    else:
        domain_dot_index = string.find('.', atsign_index)
        domain_dot_present = domain_dot_index >= 0
        return domain_dot_present

def text_present(string):
    if string != "":
        return True
    else:
        return False      

def blank_space(string):
    blank_space = " "
    if blank_space in string:
        return True
    else:
        return False  

#@app.route("/")
#def mainpage():
#    return render_template('signup.html')

@app.route("/", methods=['POST', 'GET'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']

        error_present = False

        name_error = "" 
        name_blank_error = ""       
        name_len_error = ""
        password_error = ""
        pass_len_error = ""
        pass_blank_error = ""
        match_error = ""
        mail_error = ""

    # username validity check
        if not text_present(username):
            name_error = "This field is required. Please enter a username."
            error_present = True
  
        if blank_space(username):
            name_blank_error = "Blank spaces are not allowed. Please try again."
            error_present = True

        if len(username) > 20 or len(username) < 3:
            name_len_error = "Username must be between 3-20 characters in length."
            error_present = True

    # password validity check
        if not text_present(password):
            password_error = "This field is required. Please enter a password."
            error_present = True

        if blank_space(password):
            pass_blank_error ="Blank spaces are not allowed. Please try again."
            error_present = True

        if len(password) > 20 or len(password) < 3:
            pass_len_error = "Password must be between 3-20 characters in length."           
            error_present = True

    # re-enter password, verification check
        if password != verify:
            match_error = "Please try again. Passwords did not match."
            error_present = True


    # email validity check
    
        if not is_email(email) and not len(email)==0:
            mail_error = "Please try again. That email address is not in the correct format (@ or .)."
            error_present = True

        if blank_space(email):
            mail_error = "Please try again. That email address is not in the correct format (blank space)."
            error_present = True

        if len(email) > 20 or len(email) < 3 and not len(email)==0:
            mail_error = "Please try again. That email address is not in the correct format (length)." 
            error_present = True

    # if no errors, send to welcome page
    if error_present == True:
        return render_template("signup.html", 
        username=username,
        email=email,
        error_present=error_present,
        name_error = name_error,
        name_blank_error = name_blank_error, 
        name_len_error = name_len_error, 
        password_error = password_error, 
        pass_blank_error = pass_blank_error, 
        pass_len_error = pass_len_error, 
        match_error = match_error, 
        mail_error = mail_error)
    else:
        return render_template("welcome.html", username=username)

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()
