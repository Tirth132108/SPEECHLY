# Importing essential libraries
from types import MethodDescriptorType
from flask import Flask, render_template, request,redirect,url_for,session
from flask.helpers import flash
import pandas as pd
from google_trans_new import google_translator
from pydub import AudioSegment 
from pydub.playback import play 
import gtts 
from playsound import playsound
import datetime
import os


import speech_recognition as sr
translator = google_translator()

app = Flask(__name__)
app.secret_key = 'itsfantastic'     
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="Speechly"
)

@app.route('/')
def home():
    return redirect(url_for('login'))
@app.route('/login',methods=['POST', 'GET'])
def login():
    error = ""
    if request.method == 'POST':
        if request.form['register'] == 'Sign In':
            uname = request.form['username']
            pwd = request.form['password']
        
            cursor = mydb.cursor(dictionary=True, buffered=True)
            cursor.execute("select * from user where user_name= %s AND user_password = %s", [uname,pwd])
            account = cursor.fetchone()
            if account:
                print('You are now logged in', 'success')
                session['user'] = uname
                
                cursor.close()
                return redirect(url_for('index'))
                    

            else:
                error = 'Invalid Username or Password'
                return render_template('login.html', error=error)
        else:
            user_name = request.form['user']
            new_pwd = request.form["pass"]
            email = request.form["email"]

            cursor = mydb.cursor(dictionary=True, buffered=True)
            cursor.execute("INSERT INTO USER (user_name,user_password,user_email) VALUES (%s,%s, %s)", [user_name,new_pwd,email])
            mydb.commit()
            return render_template('login.html', error=error)

    return render_template('login.html', error=error)


@app.route('/logout', methods=['POST','GET'])
def logout():
    session.pop('user')
    return redirect(url_for('login'))

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


    

@app.route('/result', methods=['POST'])
def result():

    message = request.form['message']
    lang=request.form['languages']
    lang=lang.lower()
    if(lang=="kannada"):
        dest_code='kn'
    if(lang=="marathi"):
        dest_code='mr-in'
    if(lang=="japanese"):
        dest_code='ja'
    if(lang=="hindi"):
        dest_code='hi-in'
    if(lang=="telugu"):
        dest_code='te-in'   
    if(lang=="tamil"):
        dest_code='ta-in'
    if(lang=="gujarati"):
        dest_code='gu-in' 
    if(lang=="punjabi"):
        dest_code='pa-in'       
    #text_to_translate = translator.translate(message, src= 'en', dest= dest_code)
    text_to_translate = translator.translate(message, lang_src='en', lang_tgt=dest_code)
    text = text_to_translate
    #mytext = message
    print(dest_code)
    # Language in which you want to convert 
    #language = dest_code
      
    # Passing the text and language to the engine,  
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed 
    tts = gtts.gTTS(text)
    date_string = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
    filename = "voice"+date_string+".mp3"
    tts.save(filename)
    playsound(filename)
    mycursor = mydb.cursor()
    sql = "INSERT INTO translator (sourceMessage,translatedTo,translatedMessage) VALUES (%s,%s, %s)"
    val = (message, dest_code,text)
    mycursor.execute(sql, val)
    mydb.commit()

    return render_template("index.html", prediction=text)

if __name__ == '__main__':
	app.run(debug=True)