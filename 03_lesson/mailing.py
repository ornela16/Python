class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address  = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def address1(self,):
        address1 = self.to_address

    def address2(self):
        address2 = self.from_address

    def mailing (self):
         return f"{self.to_address},{self.from_address},{self.cost},{self.track}"


