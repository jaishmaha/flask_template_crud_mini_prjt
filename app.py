from flask import Flask,render_template,request,redirect,url_for,session

app= Flask(__name__)
app.secret_key='maha@27'

Student_list = [{"Name":"Sivapackia","Age":22 ,"Roll_NO": 101, "Marks":[90,75,80,98,65]},{"Name":"Siva","Age":21 ,"Roll_NO": 102, "Marks":[90,75,80,78,99]},
                {"Name":"Vilobin","Age":21 ,"Roll_NO": 103, "Marks":[94,75,80,88,35]},{"Name":"Mahadevi","Age":27 ,"Roll_NO": 104, "Marks":[70,85,80,98,35]},          
                {"Name":"Nisha","Age":23 ,"Roll_NO": 105, "Marks":[90,75,85,98,35]},{"Name":"Vaisali","Age":27 ,"Roll_NO": 106, "Marks":[80,98,35,90,75]},
                {"Name":"Vijay","Age":22 ,"Roll_NO": 107, "Marks":[90,80,98,35,75]},{"Name":"Mohamed Ismail","Age":22 ,"Roll_NO": 108, "Marks":[75,80,90,98,35]},
                ]

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/home',methods=['GET','POST'])
def home():
    return render_template('home.html',Student_list=Student_list)

@app.route('/login',methods=['GET','POST'])
def login():
    User="maha"
    Pword="1234"
    if request.method=='POST':
        userName=request.form.get('userName')
        password=request.form.get('password')
        if User==userName and Pword==password:
            session['User']=userName
            return redirect(url_for('home'))
        else:
            return 'Incorrect UserName or Password'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('userName',None)
    return redirect(url_for('index'))

@app.route('/AddStudent',methods=['GET','POST'])
def addStudent():    
    if request.method == 'POST':
        Name=request.form.get('Name') 
        Age=request.form.get('Age')
        RollNo=request.form.get('RollNo')
        Subject_1=request.form.get('Subject-1')
        Subject_2=request.form.get('Subject-2')
        Subject_3=request.form.get('Subject-3')
        Subject_4=request.form.get('Subject-4')
        Subject_5=request.form.get('Subject-5')
        Marks=[]
        Marks[0:5]=[Subject_1,Subject_2,Subject_3,Subject_4,Subject_5]
        #store the user's input into a dictionary
        student_dict={}
        student_dict.update({'Name':Name})
        student_dict.update({'Age':Age})
        student_dict.update({'Roll_NO':RollNo})
        student_dict.update({'Marks':Marks})
        #append the dict to list
        Student_list.append(student_dict)

        return redirect(url_for('home'))

    return render_template('addStudent.html',Student_list=Student_list)

@app.route('/editStudent/<int:index>',methods=['GET','POST'])
def editStudent(index):
    if request.method == 'POST':
        Name=request.form.get('Name') 
        Age=request.form.get('Age')
        RollNo=request.form.get('RollNo')
        Subject_1=request.form.get('Subject-1')
        Subject_2=request.form.get('Subject-2')
        Subject_3=request.form.get('Subject-3')
        Subject_4=request.form.get('Subject-4')
        Subject_5=request.form.get('Subject-5')

        Marks=[]
        Marks=[Subject_1,Subject_2,Subject_3,Subject_4,Subject_5]

        student= Student_list[index-1]  # if the s.no is 1 that index position will be 0 in the Student_list

        student['Name']=Name
        student['Age']=Age
        student['Roll_NO']=RollNo
        student['Marks']=Marks

        return redirect(url_for('home'))
    studentToEdit=Student_list[index-1]
    return render_template('editStudent.html',Student_list=studentToEdit)

@app.route('/delete/<int:index>',methods=['GET','POST'])
def deleteStudent(index):
    Student_list.pop(int(index-1))
    return redirect(url_for('home'))

    

if __name__ == "__main__":
    app.run(debug=True)