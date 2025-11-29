class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.a = big
        self.b = medium
        self.c = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            self.a -= 1
            if self.a >= 0:
                return True
        if carType == 2:
            self.b -= 1
            if self.b >= 0:
                return True
        if carType == 3:
            self.c -= 1
            if self.c >= 0:
                return True
        return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)