class Solution:
    def getbin(self,x):
        return bin(int(x))[2:]
    def convertDateToBinary(self, date: str) -> str:
        return '-'.join(self.getbin(x) for x in date.split('-'))