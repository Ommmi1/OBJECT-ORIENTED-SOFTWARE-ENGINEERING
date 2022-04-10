class WebPage:
    def __init__(self, theme):
        self.theme = theme
        def getContent(self):
        pass
class About(WebPage):
    _theme = None
    def __init__(self, theme):
        self.theme = theme
    def getContent(self):
        return "About page in " + self.theme.getColor()
class Careers(WebPage):
    _theme = None
    def __init__(self, theme):
        self.theme = theme
    def getContent(self):
        return "Careers page in " + self.theme.getColor()
class Theme:
    def getColor(self):
        pass
class DarkTheme(Theme):
    def getColor(self):
        return 'Dark Black'
class LightTheme(Theme):
    def getColor(self):
        return 'Off White'
class AquaTheme(Theme):
    def getColor(self):
        return 'Light Blue'
if __name__ == '__main__':
    darkTheme = DarkTheme()
    lightTheme = LightTheme()
    about = About(darkTheme)
    careers = Careers(darkTheme)
    aboutLight = About(lightTheme)
    careersLight = Careers(lightTheme)
    print (about.getContent())
    print (careers.getContent())
    print(aboutLight.getContent())
    print(careersLight.getContent())



class Door:
    def getDescription(self):
        pass
class WoodenDoor(Door):
    def getDescription(self):
        print ('I am a wooden door')
class IronDoor(Door):
    def getDescription(self):
        print ('I am an iron door')
class DoorFittingExpert:
    def getDescription(self):
        pass
class Welder(DoorFittingExpert):
    def getDescription(self):
        print ('I can only fit iron doors')
class Carpenter(DoorFittingExpert):
    def getDescription(self):
        print ('I can only fit wooden doors')
class DoorFactory:
    def makeDoor(self):
        pass
    def makeFittingExpert(self):
        pass
class WoodenDoorFactory(DoorFactory):
    def makeDoor(self):
        return WoodenDoor()
    def makeFittingExpert(self):
        return Carpenter()
class IronDoorFactory(DoorFactory):
    def makeDoor(self):
        return IronDoor()
    def makeFittingExpert(self):
        return Welder()
if __name__ == '__main__':
    woodenFactory = WoodenDoorFactory()
    door = woodenFactory.makeDoor()
    expert = woodenFactory.makeFittingExpert()
    door.getDescription()
    expert.getDescription()
    ironFactory = IronDoorFactory()
    door = ironFactory.makeDoor()
    expert = ironFactory.makeFittingExpert()
    door.getDescription()
    expert.getDescription()


class Pizza(object):
    def __init__(self):
        self._price = None
    def get_price(self):
        return self._price
class MexicanPizza(Pizza):
    def __init__(self):
        self._price = 8.5
class DeluxePizza(Pizza):
    def __init__(self):
        self._price = 10.5
class HawaiianPizza(Pizza):
    def __init__(self):
        self._price = 11.5
class PizzaFactory(object):
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == 'Mexican':
            return MexicanPizza()
    elif pizza_type == 'Deluxe':
        return DeluxePizza()
    elif pizza_type == 'Hawaiian':
        return HawaiianPizza()
if __name__ == '__main__':
    for pizza_type in ('Mexican', 'Deluxe', 'Hawaiian'):
    print('Price of {0} is {1}'.format(pizza_type, 
    PizzaFactory.create_pizza(pizza_type).get_price()))