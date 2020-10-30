import os
from flask import Flask, request, abort, jsonify

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


@app.route('/upload',methods = ['POST'])
def upload():
    data = "ll file saved"
    if request.method == 'POST': # Checks if it's a POST request
        uploaded_file = request.files['upload']
        llname=request.form['llname']
        file_ext = os.path.splitext(llname)[1]
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], llname))
        response = jsonify(data) 
        response.status_code = 202 
        return response 

if __name__ == '__main__':
    app.run()