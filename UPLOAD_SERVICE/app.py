import os
from flask import Flask, request, abort, jsonify
import subprocess
import shlex
import json

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.ll' ]
app.config['UPLOAD_PATH'] = os.getenv('UPLOAD_PATH','./')
app.config['OPT'] = os.getenv('OPT','opt')

@app.route('/')
def hello():
    htmlstring="""
    <html>
    <form method="post"
     action="/upload"
      enctype = "multipart/form-data"
    >
    <p>what to upload XX?</p>
    <input type="text" name="llname"></input>

    <input type="file" name="upload">  
        <input type="submit"></input>

     </form>
     </html>
    """
    return htmlstring



@app.route('/upload',methods = ['POST'])
def upload():
    data = "ll file saved"
    if request.method == 'POST':
        uploaded_file = request.files['upload']
        llname=request.form['llname']
        file_ext = os.path.splitext(llname)[1]
        if uploaded_file.filename != '':
            __filename=os.path.join(app.config['UPLOAD_PATH'], llname)
            uploaded_file.save(__filename)
            saveOptRun(__filename)
        response = jsonify(data) 
        response.status_code = 202 
        return response 


def saveOptRun(filename):
    agiantstr = app.config['OPT']+ "  -disable-output  ./{0} -passes=helloworld".format(filename)
    result = subprocess.run( shlex.split(agiantstr) , capture_output=True, text=True)
    info_jsonarray =  '['+result.stdout[:-1]+']'
    __filename=os.path.join(app.config['UPLOAD_PATH'], filename+".json")

    with open( __filename   , "w") as outfile:
        outfile.write(info_jsonarray)
        outfile.close()
    return


if __name__ == '__main__':
    app.run()