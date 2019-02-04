import uuid, os
from flask import *
from modules.json_op import *

# Server Port
PORT = 2323

# Username and Password
USERNAME = "admin"
PASSWORD = ""

app = Flask(__name__)
app.secret_key = os.urandom(24)


def check_auth():
	if 'username' in session:
		return True
	else:
		return False


@app.route("/")
def index():
	tol_data, pre_data = open_file()
	is_logged_in = False
	
	if check_auth():
		is_logged_in = True
	
	preid_list = list([])
	pre_list = list([])
	for each in pre_data:
		pre_list.append(pre_data[each])
		preid_list.append(str(each))

	return render_template("index.html", pre_costs=pre_list, tol_costs=tol_data, pre_cost_id=preid_list, length=len(
		preid_list), loggedin=is_logged_in)


@app.route("/login", methods=['POST'])
def login():
	if request.method == "POST":
		if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
			session['username'] = USERNAME
			return redirect(url_for('index'))
		else:
			flash("Wrong Username/Password!")
			return redirect(url_for('index'))


@app.route("/logoff", methods=['POST'])
def logoff():
	session.clear()
	return redirect(url_for("index"))


@app.route("/add", methods=['GET'])
def add():
	if not check_auth():
		flash("↑ Please login first")
		return redirect(url_for('index'))
	
	name = request.values.get("CostName")
	moneytype = request.values.get("MoneyType")
	money = request.values.get("CostMoney")
	comment = request.values.get("CostComment")
	if name == "" or money == "":
		return redirect(url_for('index'))
	
	tol_data, pre_data = open_file()
	
	tol_data[moneytype] = str(round(float(tol_data[moneytype]) + float(money), 2))
	pre_data[str(uuid.uuid1())] = [name, moneytype, money, comment]
	
	save_file(tol_data, pre_data)
	
	return redirect(url_for('index'))


@app.route("/del", methods=['GET'])
def delete():
	if not check_auth():
		flash("↑ Please login first")
		return redirect(url_for('index'))
	
	id = request.values.get("ID")
	
	tol_data, pre_data = open_file()
	
	tol_data[pre_data[id][1]] = str(round(float(tol_data[pre_data[id][1]]) - float(pre_data[id][2]), 2))
	pre_data.pop(id)
	
	save_file(tol_data, pre_data)
	
	return redirect(url_for('index'))


if __name__ == "__main__":
	app.run(port=PORT)
