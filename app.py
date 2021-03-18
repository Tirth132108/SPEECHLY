# Importing essential libraries
from flask import Flask, render_template, request,redirect,url_for
import speech_recognition as sr

app = Flask(__name__)

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="Speechly"
)

@app.route('/login',methods=['POST', 'GET'])
def login():
    error = ""
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
    
        cursor = mydb.cursor(dictionary=True, buffered=True)
        cursor.execute("SELECT * from user where user_name= %s AND user_password = %s", [uname,pwd])
        account = cursor.fetchone()
        if account:
            print('You are now logged in', 'success')
            cursor.close()
            return redirect(url_for('index'))
                

        else:
            error = 'Invalid Username or Password'
            return render_template('login.html', error=error)
    return render_template('login.html', error=error)
        
        
        

@app.route('/index',methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        f = request.files['audio_data']
        with open('audio.wav', 'wb') as audio:
            f.save(audio)
        print('file uploaded successfully')
        

        return render_template('index.html', request="POST")
        
         

    else:
        return render_template("index.html")
	#return render_template('index.html')

def convert():
    r = sr.Recognizer()
    with sr.AudioFile('audio.wav') as source:
        print("Say Something.....")
        audio = r.listen(source)
        print("recognizing......")
        try:
            from translate import Translator
            translator = Translator(to_lang='gujarati')
            translation = translator.translate(r.recognize_google(audio))
            print(translation)
            return translation

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


@app.route('/predict', methods=['POST'])
def predict():
    result = convert()
    mycursor = mydb.cursor()
    sql = "INSERT INTO translator (sourceMessage,translatedTo) VALUES (%s,%s)"
    val = ('user','gujarati')
    mycursor.execute(sql, val)
    mydb.commit()

    return render_template('index.html', prediction=result)    



if __name__ == '__main__':
	app.run(debug=True)
