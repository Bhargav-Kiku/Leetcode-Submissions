class RideSharingSystem:

    def __init__(self):
        self.r = deque()
        self.d = deque()
        self.c = set()


    def addRider(self, riderId: int) -> None:
        if riderId in self.c:
            self.c.remove(riderId)
        self.r.append(riderId)

    def addDriver(self, driverId: int) -> None:
        self.d.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        while self.r and self.r[0] in self.c:
            self.r.popleft()
        if self.r and self.d:
            return [self.d.popleft(), self.r.popleft()]
        else:
            return [-1, -1]

    def cancelRider(self, riderId: int) -> None:
        self.c.add(riderId)


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)