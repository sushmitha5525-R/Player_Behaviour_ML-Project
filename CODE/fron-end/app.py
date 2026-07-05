from flask import Flask,url_for,redirect,render_template,request
import mysql.connector

app  = Flask(__name__)
app.secret_key = 'admin'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

def executionquery(query,values):
    mycursor.execute(query,values)
    mydb.commit()
    return



mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
    database='db'
)

mycursor = mydb.cursor()

def executionquery(query,values):
    mycursor.execute(query,values)
    mydb.commit()
    return

def retrivequery1(query,values):
    mycursor.execute(query,values)
    data = mycursor.fetchall()
    return data

def retrivequery2(query):
    mycursor.execute(query)
    data = mycursor.fetchall()
    return data

@app.route('/register' ,methods = ['GET',"POST"])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        c_password = request.form['c_password']
        if password == c_password:
            query = "SELECT UPPER(email) FROM users"
            email_data = retrivequery2(query)
            email_data_list = []
            for i in email_data:
                email_data_list.append(i[0])
            if email.upper() not in email_data_list:
                query = "INSERT INTO users (name,email, password) VALUES ( %s, %s, %s)"
                values = (name,email, password)
                executionquery(query, values)
                return render_template('login.html', message="Successfully Registered!")
            return render_template('register.html', message="This email ID is already exists!")
        return render_template('register.html', message="Conform password is not match!")
    return render_template('register.html')
    



@app.route('/login',methods = ["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        
        query = "SELECT UPPER(email) FROM users"
        email_data = retrivequery2(query)
        email_data_list = []
        for i in email_data:
            email_data_list.append(i[0])

        if email.upper() in email_data_list:
            query = "SELECT UPPER(password) FROM users WHERE email = %s"
            values = (email, )
            password__data = retrivequery1(query, values)
            if password.upper() == password__data[0][0]:
                global user_email
                user_email = email
                return render_template('home.html')
            return render_template('login.html', message= "Invalid Password!!")
        return render_template('login.html', message= "This email ID does not exist!")
    return render_template('login.html')
    

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/model1',methods =["GET","POST"])
def model1():
    if request.method == "POST":
        algorithams = request.form["algo"]
        if algorithams == "1":
            accuracy = 95
            msg = 'Accuracy  for DecisionTree Classifier is ' + str(accuracy) + str('%')
        elif algorithams == "2":
            accuracy = 95
            msg = 'Accuracy  for RandomForestClassifier is ' + str(accuracy) + str('%')
        elif algorithams == "3":
            accuracy = 83
            msg = 'Accuracy  for LogisticRegression is ' + str(accuracy) + str('%')
        elif algorithams == "4":
            accuracy = 67
            msg = 'Accuracy  for GradientBoostingClassifier is ' + str(accuracy) + str('%')
        elif algorithams == "5":
            accuracy = 88
            msg = 'Accuracy  for Artificial_Nural_Network  is ' + str(accuracy) + str('%')
        elif algorithams == "6":
            accuracy = 85
            msg = 'Accuracy  for  Deep_Nural_Network is ' + str(accuracy) + str('%')
        else:
            accuracy = 0
            msg = "select the alogorithm"
        return render_template('model1.html',msg=msg,accuracy = accuracy)
    return render_template('model1.html')

@app.route('/model2',methods =["GET","POST"])
def model2():
    if request.method == "POST":
        algorithams = request.form["algo"]
        if algorithams == "1":
            accuracy = 99
            msg = 'Accuracy  for DecisionTree Classifier is ' + str(accuracy) + str('%')
        elif algorithams == "2":
            accuracy = 99
            msg = 'Accuracy  for  XBoostingClassifier is ' + str(accuracy) + str('%')
        elif algorithams == "3":
            accuracy = 87
            msg = 'Accuracy  for LogisticRegression is ' + str(accuracy) + str('%')
        elif algorithams == "4":
            accuracy = 100
            msg = 'Accuracy  for RandomForestClassifier is ' + str(accuracy) + str('%')
        elif algorithams == "5":
            accuracy = 81
            msg = 'Accuracy  for Artificial_Nural_Network  is ' + str(accuracy) + str('%')
        elif algorithams == "6":
            accuracy = 84
            msg = 'Accuracy  for  Deep_Nural_Network is ' + str(accuracy) + str('%')
        else:
            accuracy = 0
            msg = "select the alogorithm"
        return render_template('model2.html',msg=msg,accuracy = accuracy)
    return render_template('model2.html')


@app.route('/prediction1',methods =["GET","POST"])
def prediction1():
    if request.method == "POST":
        Daily_Active_Time = float(request.form['Daily_Active_Time'])
        In_Game_Currency_Earned = int(request.form['In_Game_Currency_Earned'])
        Purchase_History = int(request.form['Purchase_History'])
        Time_of_Purchase = int(request.form['Time_of_Purchase'])
        Churn_Rate = float(request.form['Churn_Rate'])
        In_Game_Purchases =  float(request.form['In_Game_Purchases'])
        Discount_Utilization = int(request.form['Discount_Utilization'])
        Quest_Completion_Rate = float(request.form['Quest_Completion_Rate'])

        leee = [[Daily_Active_Time,In_Game_Currency_Earned,Purchase_History,Time_of_Purchase,Churn_Rate,In_Game_Purchases,Discount_Utilization,Quest_Completion_Rate]]

        print(leee)

        import joblib
        model = joblib.load('random_forest_model_p_engage.joblib')
        prediction1 = model.predict(leee)
        if prediction1 == 0:
            result = 'Low Engagement Leval'
            return render_template('prediction1.html', result = result)
        elif prediction1 == 1:
            result = 'High Engagement Leval'
            return render_template('prediction1.html', result = result)
    return render_template('prediction1.html')
     

    

@app.route('/prediction2',methods =["GET","POST"])
def prediction2():
    if request.method == "POST":
        Daily_Active_Time = float(request.form['Daily_Active_Time'])
        In_Game_Currency_Earned = int(request.form['In_Game_Currency_Earned'])
        Purchase_History = int(request.form['Purchase_History'])
        Time_of_Purchase = int(request.form['Time_of_Purchase'])
        Churn_Rate = float(request.form['Churn_Rate'])
        In_Game_Purchases =  float(request.form['In_Game_Purchases'])
        Discount_Utilization = request.form['Discount_Utilization']
        Quest_Completion_Rate = float(request.form['Quest_Completion_Rate'])

        leee2 = [[Daily_Active_Time,In_Game_Currency_Earned,Purchase_History,Time_of_Purchase,Churn_Rate,In_Game_Purchases,Discount_Utilization,Quest_Completion_Rate]]

        print(leee2)

        import joblib
        model2 = joblib.load('random_forest_model_p_engage.joblib')
        prediction2 = model2.predict(leee2)
        if prediction2 == 0:
            result = 'Low Purchase Liklyhood'
            return render_template('prediction2.html', result = result)
        elif prediction2 == 1:
            result = 'High Purchase Liklyhood'
            return render_template('prediction2.html', result = result)
    return render_template('prediction2.html')

    



if __name__ == '__main__':
    app.run(debug=True)