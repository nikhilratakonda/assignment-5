from flask import Flask, jsonify, render_template, request
from redis import Redis
from flask import abort
import json

app = Flask(__name__)
myJsonData =  {
	"summary":[
		{"Team":"India", "Home Wins": "32", "Home Draws":"8", "Home Losses": "12"},
		{"Team":"Australia", "Home Wins": "41", "Home Draws":"12", "Home Losses": "10"}
	],
	"odi":[
		{"Date":"12 Mar", "Year":2015, "HomeTeam":"Australia", "AwayTeam":"India", "Score":"328-7 (50) - 233 (42.1)"},
		{"Date":"26 Jan", "Year":2016, "HomeTeam":"Australia", "AwayTeam":"India", "Score":"330-7 (50) - 309 (49)"},
		{"Date":"17 Sep", "Year":2017, "HomeTeam":"India", "AwayTeam":"Australia", "Score":"281-7 (50) - 137 (21)"},
		{"Date":"18 Jan", "Year":2019, "HomeTeam":"Australia", "AwayTeam":"India", "Score":"298-9 (50) - 299-4 (49.2)"},
		{"Date":"14 Jan", "Year":2020, "HomeTeam":"India", "AwayTeam":"Australia", "Score":"255 (49.1) - 258-0 (37.4)"}
	],
	"test":[
		{"Date":"15 Dec", "Year":2014, "HomeTeam":"Australia", "AwayTeam":"India", "Score":"517-7d & 290-5d - 444 & 315"},
		{"Date":"26 Dec", "Year":2018, "HomeTeam":"Australia", "AwayTeam":"India", "Score":"151 & 261 - 443 & 106-8"},
		{"Date":"6 Dec", "Year":2019, "HomeTeam":"Australia", "AwayTeam":"India", "Score":"416 & 168 - 244 & 36-9"},
		{"Date":"17 Dec", "Year":2020, "HomeTeam":"Australia", "AwayTeam":"India", "Score":"195 & 200 - 326 & 70-2"},
		{"Date":"26 Aug", "Year":2021, "HomeTeam":"England", "AwayTeam":"India", "Score":"191 & 120 - 364 & 104-2"}
	],
	"t20":[
		{"Date":"31 Jan", "Year":2016, "HomeTeam":"India", "AwayTeam":"Australia", "Score":"188-3 (18.3) - 186-5 (20)"},
		{"Date":"10 Oct", "Year":2017, "HomeTeam":"India", "AwayTeam":"Australia", "Score":"118-4 (15.3) - 117-4 (20)"},
		{"Date":"21 Nov", "Year":2018, "HomeTeam":"Australia", "AwayTeam":"India", "Score":"164-6 (20) - 168-4 (20)"},
		{"Date":"25 Feb", "Year":2019, "HomeTeam":"India", "AwayTeam":"Australia", "Score":"190-4 (20) - 194-3 (19.4)"},
		{"Date":"4 Dec", "Year":2020, "HomeTeam":"Australia", "AwayTeam":"India", "Score":"194-5 (20) - 195-4 (20)"}
	]
}#json.loads(open('./cricket.json').read())

summaryData = myJsonData["summary"]
odiData = myJsonData["odi"]
testData = myJsonData["test"]
t20Data = myJsonData["t20"]


@app.route("/", methods=['GET'])
def get_sum():
	sumList = []
	for element in summaryData:
		sumList.append(element)
	return render_template("summary.html", display_data=sumList)

@app.route("/odi", methods=['GET'])
def get_odi():
	# odiList = [element for element in odiData]
	
	return render_template("odi.html", display_data=[element for element in odiData])

@app.route("/test", methods=['GET'])
def get_test():
	testList = []
	for element in testData:
		testList.append(element)
	return render_template("test.html", display_data=testList)

@app.route("/t20", methods=['GET'])
def get_t20():
	testList = []
	for element in t20Data:
		testList.append(element)
	return render_template("test.html", display_data=testList)

@app.route("/odi/<int:year>/", methods=['GET'])
def get_odi_yr(year):
	myyrlist = []
	for element in odiData:
		if element["Year"] == year:
			myyrlist.append(element)
	return render_template("odi.html", display_data=myyrlist)

@app.route("/test/<int:year>/", methods=['GET'])
def get_test_yr(year):
	myyrlist = []
	for element in testData:
		if element["Year"] == year:
			myyrlist.append(element)
	return render_template("test.html", display_data=myyrlist)


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=80, debug=True)
