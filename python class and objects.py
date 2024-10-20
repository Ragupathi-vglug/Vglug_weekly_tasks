#BASIC class and object creation
class vehicle:
    def tata(brand,color,model):
        print("Model is:",model)
        print("Color is:",color)
        print("Brand is:",brand)
cars=vehicle
cars.tata("tata1761","navy blue","tata")

#PROGRAM FOR ENCAPSULATION
class cars:
    def __init__(self,car):
            self.car=car
        
    def list_cars(self):
        print("Available cars")
        for cars_list in self.car:
            print(cars_list)
            
    def borrow_car(self,buying_car):
        
        if buying_car in self.car:
            print("Get your car")
            self.car.remove(buying_car) 
        else:
            print("The car is not Available")
available_cars=["Maruti Suzuki","Hyundai","Tata Motors","Mahindra","Kia","Toyota","MG Motor","Honda","Renault","Skoda"]
designs=cars(available_cars)
presentation="""
1.Display cars
2.Borrow car
"""
while True:
    print(presentation)
    
    choice=int(input("Enter your choice:"))
    if choice==1:
        designs.list_cars()
    
    elif choice==2:
        a=input("Enter the  car name:")
        designs.borrow_car(a)
    else:
        break;    
