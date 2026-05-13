class WeatherStation:
    def __init__(self):
        self.observers = []

    def add_subscribers(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_subscribers(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self, temprature):
        for observer in self.observers:
            observer.update(temprature)

class PhoneDisplay():
    def __init__(self, name):
        self.name = name

    def update(self, temprature):
        print(f"{self.name}'s display: {temprature}")

# ==================

me = WeatherStation()

willo = PhoneDisplay("willow")
me.add_subscribers(willo)

kaber = PhoneDisplay("kabeer")
me.add_subscribers(kaber)

arayan = PhoneDisplay("arayan")
me.add_subscribers(arayan)

aiden = PhoneDisplay("aiden")
me.add_subscribers(aiden)

me.notify(-8)

me.remove_subscribers(aiden)

me.notify(-12)
