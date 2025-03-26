class car():
    def __init__(self,color,speed,make,model):
        self.__color=color
        self.__speed=speed
        self.make=make
        self.model=model
        
        
    def info(self):
        return f'the color of car is  {self.get_color()}   and the speed of car is  {self.get_speed()}'
    def get_speed(self):
        return self.__speed
    def set_speed(self,speedvalue):
        if speedvalue >0:
            self.__speed=speedvalue
        else :
            self.__speed=0
    def get_color(self):
        return self.__color
    def set_color(self,colorvalue='white'):
        self.__color=colorvalue
					

class ElectricCar(car):
    def __init__(self,color,speed,make,model,battery_capacity ):
        super().__init__(color,speed,make,model)
        self.battery =Battery(battery_capacity )

    def info(self):
        base=super().info()

        return f'{base}, battery capacity is {self.battery.get_capacity()} kWh, charge level is {self.battery.get_charge_level()}%'
    def batterycharge(self,amount):
        return self.battery.charge(amount)
    
    def batterydischarge(self,amount):
        return self.battery.discharge(amount)

    def calculaterange(self):
        permilesrange=3
        range= self.battery.get_capacity()/permilesrange
        return f'The estimated range of the car is {range} miles on a full charge.'
class sportscar(car):
    def __init__(self, color, speed, make, model,maxspeed,acceleration):
        super().__init__(color, speed, make, model)
        self.maxspeed=maxspeed
        self.acceleration=acceleration
    def info(self):
        baseinfo=super().info()
        return f'{baseinfo}, max speed is {self.max_speed} mph, and acceleration 0-60 mph in {self.acceleration} seconds'
        
    def performance(self):
        if self.acceleration>=6:

            return "This sports car has supercar-level performance."
        elif self.acceleration <= 6:
            return "This sports car has excellent performance."
        else:
            return "This sports car has average performance."
        
class Battery():
    def __init__(self,capacity,charge_level=100):
        self.capacity=capacity
        self.charge_level=charge_level
    
    def charge(self,amount):
        if self.charge_level+amount <=100:
            self.charge_level=self.charge_level+amount 
        else:
            self.charge_level=100
        return f'battery charge {self.charge_level}%'
    
    def discharge(self,amount):
        if self.charge_level-amount >=0:
            self.charge_level=self.charge_level-amount 
        else:
            self.charge_level = 0
        return f'Battery discharged to {self.charge_level}%'
    
    def get_charge_level(self):
        return self.charge_level
    
    def get_capacity(self):
        return self.capacity




obj1=ElectricCar('red',200,'tesla','s1',9000)
print(obj1.batterycharge(10))
# print(obj1.calculaterange())
# obj1=car('red',200,'tesla','s1')
# print(obj1.info())
# obj1.set_speed(8000)
# print(obj1.info())

# obj3=sportscar("red",120,"tesla","s3",300,6)

# print(obj3.performance())
