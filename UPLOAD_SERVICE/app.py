import os
from flask import Flask, request, abort, jsonify
import subprocess
import shlex
import json

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.ll' ]
app.config['UPLOAD_PATH'] = './'

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


@app.route('/upload0',methods = ['POST'])
def upload0():
    data = "ll file saved"
    if request.method == 'POST':
        uploaded_file = request.files['upload']
        llname=request.form['llname']
        file_ext = os.path.splitext(llname)[1]
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], llname))
        response = jsonify(data) 
        response.status_code = 202 
        return response 

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
    agiantstr =  "../build/bin/opt  -disable-output  ./{0} -passes=helloworld".format(filename)
    result = subprocess.run( shlex.split(agiantstr) , capture_output=True, text=True)
    infostr = result.stdout
    infoList = splitOptOutput(infostr)
    with open("./"+ filename+".json", "w") as outfile:
        json.dump(infoList, outfile)
    return

def splitOptOutput(_infostr):
    resultList=[]
    a1=_infostr.split("End HelloWorldPass\n" )
    a2=  [i for i in a1 if i] 
    for a in a2:
        methodDictionary={}
        splitArr0 = a.split("\n")[1:]
        methodDictionary['function']=splitArr0[0].split(":")[1].strip()
        methodDictionary['rettype']=splitArr0[1].split(":")[1].strip()
        methodDictionary['cconv']=splitArr0[2].split(":")[1].strip()
        methodDictionary['isns']=splitArr0[3].split(":")[1].strip()
        resultList.append(methodDictionary)
    # print("resultList is {0}".format(resultList))
    return resultList



if __name__ == '__main__':
    app.run()