class Wallet:
    def __init__(self, couleur, isLost):
        self.couleur = couleur
        self.isLost = isLost


    def addVola(self):
        print("Add vola")

    def getVola(self):
        print("Get Vola")

    def open(self):
        print("open")

    def close(self):
        print("close")

    def checkVola(self):
        print("check vola")



portVola = Wallet("rouge", False)