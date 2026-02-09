class Node:
    def __init__(self):
        self.val = None
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.ll = Node()
        self.ll.val = homepage

    def visit(self, url: str) -> None:
        nn = Node()
        nn.val = url
        nn.prev = self.ll
        self.ll.next = nn
        self.ll = self.ll.next

    def back(self, steps: int) -> str:
        x = steps
        while self.ll.prev and x:
            self.ll = self.ll.prev
            x -= 1
        return self.ll.val

    def forward(self, steps: int) -> str:
        x = steps
        while self.ll.next and x:
            self.ll = self.ll.next
            x -= 1
        return self.ll.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)