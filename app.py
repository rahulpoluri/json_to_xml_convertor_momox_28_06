from flask import Flask, render_template, request, url_for, redirect, Response, flash
from xml_to_json_convertor import *
import requests
import random

from flask import Flask
app = Flask(__name__)

ALLOWED_EXTENSIONS = ["xml"]

def allowed_file(filename):
   return '.' in filename and \
          filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def get_dish_id():
   pass

@app.route('/', methods=['GET', 'POST'])
def uploadXmlFile():
   if request.method == 'POST':
      # check if the post request has the file part
      if 'file' not in request.files:
         flash('No file part')
         return redirect(request.url)

      file = request.files['file']
      # if user does not select file, browser also
      # submit an empty part without filename
      if file.filename == '':
         flash('No selected file')
         return redirect(request.url)
      if file and allowed_file(file.filename):
         filename = "xml"+ str(random.randomint)+ ".xml"
         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
         return convertEmployeesInfoXmlToOrdersJson(file)
   return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
   app.run()





