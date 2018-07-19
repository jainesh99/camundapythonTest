import requests
import json
import socket


class FetchAndLock:

    response = ""
    response_dict=""

    def createjson(self, topic, lockduration):
        data = {
                "workerId": socket.gethostname(),
                "maxTasks": 10,
                "topics": [
                    {
                        "topicName": topic,
                        "lockDuration": lockduration,
                        "variables": None,
                        "businessKey": None
                    }
                    ]
                }

        return data

    def sendjson(self, topic, lockduration, host):
        self.response = requests.post('http://' + host + '/engine-rest/external-task/fetchAndLock',
                                      json=self.createjson(topic=topic, lockduration=lockduration))
        return self.response

    def getresponsetext(self):
        return self.response.text

    def storereponseindict(self):
        self.response_dict = json.loads(self.response.text)

    def getvariable(self,str):
        return self.response_dict[0]["variables"][str]['value']

    def getid(self):
        return self.response_dict[0]["id"]
