from abc import ABC,abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
    @abstractmethod 
    def info(self):
        pass


class car(vehicle):

    def __init__(self,colour,speed,model,make):
        self.colour=colour
        self.__speed=speed
        self.model=model
        self.make=make

    def start_engine(self):
        return "Car engine started"
    
    def stop_engine(self):
        return "Car engine stopped"
    def get_speed(self):
         return self.__speed
         
    
    def info(self):
                return f'Car: {self.make} {self.model}, Color: {self.colour}, Speed: {self.get_speed()} mph'



a=car('red',120,'mustang','ford')
print(a.info())