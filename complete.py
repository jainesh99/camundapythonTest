import requests
import socket

class Complete:

    response=""

    def createcompletejson(self):
        data = {
                "workerId": socket.gethostname(),
                "variables": {
                    "aVariable": {
                        "value": "Paul"
                    },
                    "anotherVariable": {
                        "value": 69
                    },
                    "aThirdVariable": {
                        "value": True
                    }
                },
                "localVariables": {
                    "aLocalVariable": {
                        "value": "aStringValue"
                    }
                }
            }

        return data

    def sendcomplete(self, guid, host):
        self.response = requests.post('http://' + host + '/engine-rest/external-task/' + str(guid) + '/complete',
                                      json=self.createcompletejson())
        return self.response

    def getresponse(self):
        return self.response.text