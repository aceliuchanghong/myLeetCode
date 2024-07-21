"""
产品类          Car
抽象建造者       CarBuilder
具体建造者       GasolineBuilder,ElectricBuilder
导演类          CarBuilderDirector
"""


# 产品类
class Car:
    def __init__(self):
        self.engine = None
        self.wheels = None
        self.body = None

    def __str__(self):
        return f"Car(engine={self.engine}, wheels={self.wheels}, body={self.body})"


# 抽象建造者
class CarBuilder:
    def build_engine(self):
        pass

    def build_wheels(self):
        pass

    def build_body(self):
        pass

    def get_car(self):
        pass


# 具体建造者 - GasolineBuilder
class GasolineBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def build_engine(self):
        self.car.engine = "Gasoline Engine"

    def build_wheels(self):
        self.car.wheels = "Regular Wheels"

    def build_body(self):
        self.car.body = "Sedan Body"

    def get_car(self):
        return self.car


# 具体建造者 - ElectricBuilder
class ElectricBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def build_engine(self):
        self.car.engine = "Electric Engine"

    def build_wheels(self):
        self.car.wheels = "Sport Wheels"

    def build_body(self):
        self.car.body = "SUV Body"

    def get_car(self):
        return self.car


# 导演类
class CarBuilderDirector:
    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.build_engine()
        self._builder.build_wheels()
        self._builder.build_body()
        return self._builder.get_car()


if __name__ == "__main__":
    director = CarBuilderDirector(GasolineBuilder())
    gasoline_car = director.construct_car()
    print(gasoline_car)

    director = CarBuilderDirector(ElectricBuilder())
    electric_car = director.construct_car()
    print(electric_car)
