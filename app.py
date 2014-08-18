import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from werkzeug import secure_filename
from collections import OrderedDict

from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'


db = SQLAlchemy(app)

#db.create_all()
from models import *


ALLOWED_EXTENSIONS = set(['doc', 'docx', 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

#app.config['UPLOAD_FOLDER'] = 'uploads/'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('details.html')

@app.route('/staffs/<staffname>', methods=['GET'])
def staffprofile(staffname):
	if request.method == 'GET':
	    staff = Staff.query.filter_by(Staff_Name=staffname)
	    return render_template('staffprofile.html', staffname = staffname, staff = staff)
     



@app.route('/staffs', methods=['GET','POST'])
def staffs():
  if request.method == 'POST':       	
	fileurl = []
	#data = dict((key, request.form.getlist(key)) for key in request.form.keys())
	for key in request.files:
		file = request.files[key]
		if file and allowed_file(file.filename):
			if not os.path.exists('uploads/' + request.form['Staff_Name']):
    				os.makedirs('uploads/' + request.form['Staff_Name'])
			app.config['UPLOAD_FOLDER'] = 'uploads/' + request.form['Staff_Name'] + '/'
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    			fileurl.append(app.config['UPLOAD_FOLDER'] + filename)
	
	#print data
	#for k in request.form:
	#	print k + ":" + request.form[k]
		
	print fileurl[0]
	#print request.form['Staff_Name']
	
#	print request.form  #debug
	
	try:
		s = Staff(request.form['Staff_Name'], request.form['Staff_ID'],\
				request.form['Staff_Email'], request.form['Staff_Phone'],request.form['Staff_Address'], fileurl[0])
		q = Education(request.form['UG_Ins_Name'], request.form['UG_Ins_Special'],request.form['UG_Ins_Year'],request.form['UG_Attach'],\
				request.form['PG_Ins_Name'], request.form['PG_Ins_Special'],request.form['PG_Ins_Year'],request.form['PG_Attach'],\
				request.form['PHD_Ins_Name'], request.form['PHD_Ins_Special'],request.form['PHD_Ins_Year'],request.form['PHD_Attach'])
		r = Activities(request.form['Workshops'], request.form['Seminars'], request.form['EDP'])
		
		db.session.add(s)
		db.session.commit()
		staff = Staff.query.all()
	except BaseException, be:
		print "Error:", be
	#for i in staff:
	#	print i.Staff_Name
	
	#return render_template('stafflist.html', staff = staff)
        return render_template('stafflist.html', staff = staff)
  if request.method == 'GET':
	  staff = Staff.query.all()
	  return render_template('stafflist.html', staff = staff)

if __name__ == '__main__':
	app.run(
        host="0.0.0.0",
        port=int("80"),
        debug=True
    )
	

