# ---------- Vehicle Control System: Abstraction Demonstration ----------

from abc import ABC, abstractmethod

# Base abstract class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Derived class 1
class Car(Vehicle):
    def start(self):
        print("Car started with a push button ignition system.")

    def stop(self):
        print("Car stopped smoothly using ABS brakes.")


# Derived class 2
class Bike(Vehicle):
    def start(self):
        print("Bike started using kick start mechanism.")

    def stop(self):
        print("Bike stopped using disc brakes.")


# ---------- Try It Out Section ----------
vehicles = [Car(), Bike()]

for v in vehicles:
    v.start()
    v.stop()
