import uuid
from flask import *
from json_op import *

PORT = 2323

app = Flask(__name__)
app.secret_key = b'thisisareallysecretsecretkey'


@app.route("/")
def index():
	tol_data, pre_data = open_file()
	
	preid_list = list([])
	pre_list = list([])
	for each in pre_data:
		pre_list.append(pre_data[each])
		preid_list.append(str(each))
		
	return render_template("index.html", pre_costs=pre_list, tol_costs=tol_data, pre_cost_id=preid_list, length=len(preid_list))


@app.route("/add", methods=['GET'])
def add():
	name = request.values.get("CostName")
	moneytype = request.values.get("MoneyType")
	money = request.values.get("CostMoney")
	comment = request.values.get("CostComment")
	if name == "" or money == "":
		return redirect("/")
	
	tol_data, pre_data = open_file()
	
	tol_data[moneytype] = str(float(tol_data[moneytype]) + float(money))
	pre_data[str(uuid.uuid1())] = [name, moneytype, money, comment]
	
	save_file(tol_data, pre_data)
	
	return redirect("/")


@app.route("/del", methods=['GET'])
def delete():
	id = request.values.get("ID")
	
	tol_data, pre_data = open_file()
	
	tol_data[pre_data[id][1]] = str(float(tol_data[pre_data[id][1]]) - float(pre_data[id][2]))
	pre_data.pop(id)
	
	save_file(tol_data, pre_data)
	
	return redirect("/")


if __name__ == "__main__":
	app.run(port=PORT)
