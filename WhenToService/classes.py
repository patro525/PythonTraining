# Program created for training classes in python purposes
print("Welcome in 'When should you change a timing chain in your car?' program. Answer questions below:")
print("Give a number that defines your vehicle type (1-3) (1. Car | 2. Truck | 3. Bus): ")
vType = int(input())
chain = int(input("How many changes of timing chain has you vehicle had?: "))
lastChangeMileage = int(input("Type mileage when your vehicle has its last timing chain change (if never type '0'): "))
actualMileage = int(input("Type actual mileage of your vehicle: "))

class VehicleType:

    def __init__(self, vType):
        self.vType = vType
        #print("Give a number that defines your vehicle type (1-3): ")

    def vehicle(self):
        vehicleType = (["car", "truck", "bus"]) #list of available vehicles
        return "Your vehicle is a " + vehicleType[self.vType - 1] + "."

    def timingChainChange(self, chain, lastChangeMileage, actualMileage):
        self.chain = chain
        self.lastChangeMileage = lastChangeMileage
        self.actualMileage = actualMileage
        interval = actualMileage - lastChangeMileage
        basicInterval = 100000

        if self.vType == 1: #if it is a car
            if chain == 0:    
                if interval < basicInterval:
                    return "You should change your timing chain in " + str((basicInterval - interval)) + " miles."
                else:
                    return "You should change your timing chain now."
            elif chain >= 1 and chain <= 3:
                basicInterval -= 20000
                if interval < basicInterval:
                    return "You should change your timing chain in " + str((basicInterval - interval)) + " miles."
                else:
                    return "You should change your timing chain now."
            else:
                basicInterval -= 40000
                if interval < basicInterval:
                    return "You should change your timing chain in " + str((basicInterval - interval)) + " miles."
                else:
                    return "You should change your timing chain now."
        elif self.vType == 2: #if it is a truck
            basicInterval *= 5
            if chain == 0:
                if interval < basicInterval:
                    return "You should change your timing chain in " + str((basicInterval - interval)) + " miles."
                else:
                    return "You should change your timing chain now."
            elif chain >= 1 and chain <= 3:
                basicInterval -= 20000*5
                if interval < basicInterval:
                    return "You should change your timing chain in " + str((basicInterval - interval)) + " miles."
                else:
                    return "You should change your timing chain now."
            else:
                basicInterval -= 40000*5
                if interval < basicInterval:
                    return "You should change your timing chain in " + str((basicInterval - interval)) + " miles."
                else:
                    return "You should change your timing chain now."
        elif self.vType == 3: #if it is a bus
            basicInteval *= 3
            if chain == 0:
                if interval < basicInterval:
                    return "You should change your timing chain in " + str((basicInterval - interval)) + " miles."
                else:
                    return "You should change your timing chain now."
            elif chain >= 1 and chain <= 3:
                basicInterval -= 20000*3
                if interval < basicInterval:
                    return "You should change your timing chain in " + str((basicInterval - interval)) + " miles."
                else:
                    return "You should change your timing chain now."
            else:
                basicInterval -= 40000*3
                if interval < basicInterval:
                    return "You should change your timing chain in " + str((basicInterval - interval)) + " miles."
                else:
                    return "You should change your timing chain now."
        else:
            return "You picked wrong type of a vehicle."

     #def oilChange(self, oil):
      #      self.oil = oil

vehicle1 = VehicleType(vType)
print(vehicle1.vehicle())
print(vehicle1.timingChainChange(chain, lastChangeMileage, actualMileage), "\n")
