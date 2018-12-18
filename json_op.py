import json, os, platform

tolcost_path = ".\\data\\tol-cost.json"
precost_path = ".\\data\\pre-cost.json"
tolcost_path_nonWin = "./data/tol-cost.json"
precost_path_nonWin = "./data/pre-cost.json"


def decide_path():
	if platform.system() != "Windows":
		tol_path = tolcost_path_nonWin
		pre_path = precost_path_nonWin
	else:
		tol_path = tolcost_path
		pre_path = precost_path
		
	return tol_path, pre_path


def create_tolcost(path):
	tmpdic = dict({})
	tmpdic["USD"] = "0"
	tmpdic["CNY"] = "0"
	with open(path, "w", encoding='utf-8') as f:
		json.dump(tmpdic, f)


def create_precost(path):
	tmpdic = dict({})
	with open(path, "w", encoding='utf-8') as f:
		json.dump(tmpdic, f)


def open_file():
	tol_path, pre_path = decide_path()
	
	if not os.path.exists(tol_path):
			create_tolcost(tol_path)
	
	if not os.path.exists(pre_path):
			create_precost(pre_path)
	
	with open(tol_path, "r") as f:
		toldic = json.load(f)
	
	with open(pre_path, "r") as f:
		predic = json.load(f)
	
	return toldic, predic


def save_file(tol_data, pre_data):
	tol_path, pre_path = decide_path()
	
	tol_js = json.dumps(tol_data)
	pre_js = json.dumps(pre_data)
	with open(os.path.join(tol_path), "w") as f:
		f.write(tol_js)
		
	with open(os.path.join(pre_path), "w") as f:
		f.write(pre_js)
