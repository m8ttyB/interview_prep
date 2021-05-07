#!/usr/bin/env python
import random
from flask import Flask, request
import time
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class AutomoxBackend(Resource):
    def get(self):
        r = random.randint(1,100)
        if r < 80:
            return {"Message":"Good checkin"},200
        elif r < 90:
            return {"Message":"Bad request"},400
        time.sleep(random.random())
        return {"Message":"Server error"},500

api.add_resource(AutomoxBackend, '/v1/checkin')

if __name__ == "__main__":
    app.run(port=5001, host='0.0.0.0')