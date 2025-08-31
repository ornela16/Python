class Address:
    def __init__(self, index, sity, street,  house, flat):
        self.index = index
        self.sity = sity
        self.street = street
        self.house = house
        self.flat = flat

    def __str__(self):
        return(f"{self.index}, {self.sity}, {self.street}, {self.house} - {self.flat}")


