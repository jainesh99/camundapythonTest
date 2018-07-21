from fetchAndLock import FetchAndLock
from complete import Complete
import requests

class ExternalTask:

    fetch = FetchAndLock()
    complete = Complete()

    def subscribe(self, topic, lockduration, host):
        self.fetch.sendjson(topic=topic, lockduration=lockduration, host=host)

    def startautomation(self):
        if self.fetch.getresponsetext() != "[]":
            self.fetch.storereponseindict()
            return True
        else:
            return False

    def getvariable(self, str):
        return self.fetch.getvariable(str=str)

    def completeautomation(self, host):
        print(self.fetch.getid())
        print(self.complete.sendcomplete(guid=self.fetch.getid(), host=host))
        print(self.complete.getresponse())

#put local variable
    def putvariable(self, host, varname):
        json = {"value": "someValue", "type": "String"}

        putresponse = requests.put('http://' + host + '/engine-rest/execution/' + self.fetch.getexecutionid() + '/localVariables/' + varname,json=json)
        print(putresponse)
        print(putresponse.text)