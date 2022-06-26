import csv
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class KeyPlayer(Resource):
    def get(self):

        form = {}

        with open('KeyPlayersPulwama.csv', encoding="utf-8", mode="r") as csvFile:
            csvReader = csv.reader(csvFile)
            next(csvReader)
            i = 0
            for line in csvReader:
                id = line[1]
                name = line[2]
                data ={
                    "Id":id,
                    "Name":name
                }
                if i == 0:
                    form[i] = data
                    i = i+1
                else:
                    if form[i-1]!=data :
                        form[i] = data
                        i = i + 1

        return jsonify(form)


class Graph(Resource):
    def get(self):

        nodes = []
        prevnode = {
            "id" : "0",
            "label" : "0"
        }
        edges = []
        dataform = {}

        with open('KeyPlayersPulwama.csv', encoding="utf-8", mode="r") as csvFile:
            csvReaderk = csv.reader(csvFile)
            next(csvReaderk)

            for line in csvReaderk:
                Id = line[1]
                datanode = {
                    "id":Id,
                    "label":Id
                }

                if(prevnode != datanode):
                    nodes.append(datanode)
                prevnode = datanode

        with open('NetworkPulwama.csv', encoding="utf-8", mode="r") as csvFile:
            csvReadern = csv.reader(csvFile)
            next(csvReadern)

            for row in csvReadern:
                src = row[1]
                dest = row[2]
                dataedge = {
                    "from":src,
                    "to":dest
                }
                edges.append(dataedge)

        dataform[0] = nodes
        dataform[1] = edges

        return jsonify(dataform)


class TimeSeries(Resource):
    def get(self):

        datadict = {}
        datalist = []

        with open('FrequencyTable.csv', encoding="utf-8", mode="r") as csvFile:
            csvReaderts = csv.reader(csvFile)

            startrec = ["Date","Frequency"]
            datalist.append(startrec)
            next(csvReaderts)
            i = 0
            for rec in csvReaderts:
                reclist = []
                id = rec[1]
                reclist.append(id)
                name = rec[2]
                reclist.append(name)

                datalist.append(reclist)

        datadict[0] = datalist
        return jsonify(datadict)


class UserInfo(Resource):
    def get(self):
        form = {}

        with open('KeyPlayersPulwama.csv', encoding="utf-8", mode="r") as csvFile:
            csvReader = csv.reader(csvFile)
            next(csvReader)
            i = 0
            for line in csvReader:
                id = line[1]
                name = line[2]
                data ={
                    "Id":id,
                    "Name":name
                }
                if i == 0:
                    form[i] = data
                    i = i+1
                else:
                    if form[i-1]!=data :
                        form[i] = data
                        i = i + 1

        return jsonify(form)


api.add_resource(KeyPlayer, '/keyplayer/')
api.add_resource(Graph, '/graph/')
api.add_resource(TimeSeries, '/timeseries/')
api.add_resource(UserInfo, '/userinfo/')

if __name__ == '__main__':
    app.run(debug=True)
