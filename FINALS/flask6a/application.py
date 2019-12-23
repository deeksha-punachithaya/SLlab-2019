from flask import Flask, url_for, redirect, request, render_template, session

app = Flask(__name__)

app.secret_key = "secret"

@app.route("/", methods=['GET','POST'])
def index():
	if request.method == 'GET':
		msg = "Enter values"
		return render_template('index.html',msg=msg)
		
	if request.method == 'POST':
	#	if (request.form['item1'] == '' and request.form['item2'] == '' and request.form['item3'] == '') or (request.form['cost1'] == '' and request.form['cost2'] == '' and request.form['cost3'] == ''):
	#		msg = "Enter values for atleast 1 item"
	#		return render_template('index.html', msg=msg)
			
		#else:
		total=0
		one = int(request.form['cost1'])
		two = int(request.form['cost2'])
		three = int(request.form['cost3'])
		total = one + two + three
		return render_template('index.html', total=total,msg="")
			
if __name__ == '__main__':
	app.run(debug=True)		

