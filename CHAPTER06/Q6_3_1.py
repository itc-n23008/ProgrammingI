class Nigiri:
    def __init__(self):
        self.top = ""
        self.base = "しゃり"
        self.category = "にぎり"
        self.print = "100円"

    def show_attributes(self):
        print("top:", self.top)
        print("base:", self.base)
        print("category:", self.category)
        print("print:", self.print)


class Katsuo(Nigiri):
    top = "かつお"
    topping = "生姜とねぎ"

    def show_attributes(self):
        super().show_attributes()
        print("topping:", self.topping)


k1 = Katsuo()
k1.show_attributes()
