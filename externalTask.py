from fetchAndLock import FetchAndLock
from complete import Complete


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
