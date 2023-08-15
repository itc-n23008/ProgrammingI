class Katsuo(Nigiri):
    top = "かつお"
    topping = "生姜とねぎ"

    def show_attributes(self):
        super().show_attributes()
        print("topping:", self.topping)


class Nigiri:
    def show_attributes(self):
        print("top:", self.top)
        print("rice:", self.rice)
        print("neta:", self.neta)


class Maguro(Nigiri):
    top = "まぐろ"
    topping = "わさびとしょうゆ"


k1 = Katsuo()
k1.show_attributes()
