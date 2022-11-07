from flask import Flask, render_template, redirect, url_for, request
import main

app = Flask(__name__)



@app.route('/',methods = ['POST', 'GET'])
def index():
   if request.method == 'GET':
      return render_template('index.html')
   else:
      message = request.form['message']
      no = main.rating(message)
      print(no)
      return render_template('index.html',data = no)




if __name__ == '__main__':
   app.run(debug = True)