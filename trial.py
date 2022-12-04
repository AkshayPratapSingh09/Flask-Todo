class Akshay:
    def __init__(self):
        self.data = "Akshay is here right now"
        self.data2 = "Akshay was here"

    def __repr__(self) -> str:
        return self.data2

a = Akshay()
print(a)