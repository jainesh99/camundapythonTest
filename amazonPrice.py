from externalTask import ExternalTask
from pyautoguiTest import PyAutoGuiTest
import schedule

e = ExternalTask()
p = PyAutoGuiTest()

def run():
    e.subscribe("amazon-price", 10000, "10.0.0.187:8083")

    if e.startautomation():
        e.completeautomation("10.0.0.187:8083")
    else:
        print("The task is not started")


schedule.every(5).seconds.do(run)

while True:
    schedule.run_pending()