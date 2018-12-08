import json, os

tolcost_path = ".\\data\\tol-cost.json"
precost_path = ".\\data\\pre-cost.json"


def create_tolcost(path):
	tmpdic = dict({})
	tmpdic["USD"] = "0"
	tmpdic["CNY"] = "0"
	with open(path, "w", encoding='utf-8') as f:
		json.dump(tmpdic, f)


def create_precost(path):
	tmpdic = dict({})
	# tmpdic["test1"] = ["test1", "USD", "7.00", "Test1 Comment"]
	# tmpdic["test2"] = ["test2", "USD", "1.00", "Test2 Comment"]
	with open(path, "w", encoding='utf-8') as f:
		json.dump(tmpdic, f)


def open_file():
	if not os.path.exists(tolcost_path):
		create_tolcost(tolcost_path)
	
	if not os.path.exists(precost_path):
		create_precost(precost_path)
	
	with open(tolcost_path, "r") as f:
		toldic = json.load(f)
	
	with open(precost_path, "r") as f:
		predic = json.load(f)
	
	return toldic, predic


def save_file(tol_data, pre_data):
	tol_js = json.dumps(tol_data)
	pre_js = json.dumps(pre_data)
	with open(os.path.join(tolcost_path), "w") as f:
		f.write(tol_js)
		
	with open(os.path.join(precost_path), "w") as f:
		f.write(pre_js)
