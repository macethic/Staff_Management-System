import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
from collections import OrderedDict

from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

ALLOWED_EXTENSIONS = set(['doc', 'docx', 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

#app.config['UPLOAD_FOLDER'] = 'uploads/'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('details.html')

@app.route
@app.route('/upload', methods=['POST'])
def upload():
        	
	fileurl = []
	#data = dict((key, request.form.getlist(key)) for key in request.form.keys())
	for key in request.files:
		file = request.files[key]
		if file and allowed_file(file.filename):
			if not os.path.exists('uploads/' + request.form['Staff_Name']):
    				os.makedirs('uploads/' + request.form['Staff_Name'])
			app.config['UPLOAD_FOLDER'] = 'uploads/' + request.form['Staff_Name']
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    			fileurl.append(app.config['UPLOAD_FOLDER'] + filename)
	
	#print data
	for k in request.form:
		print k + ":" + request.form[k]
		
	print fileurl
	print request.form
	

	return render_template('details.html')

if __name__ == '__main__':
	app.run(
        host="0.0.0.0",
        port=int("80"),
        debug=True
    )
	

