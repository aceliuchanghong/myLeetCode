"""
桥接模式

抽象类（Abstraction）：定义了使用实现部分的接口。
细化抽象类（Refined Abstraction）：从抽象类继承，实现一部分功能，并与实现类中的对象关联。
实现者接口（Implementor）：定义实现部分的接口，包括基本操作。
具体实现（Concrete Implementor）：实现实现者接口，实现具体功能。
"""


# 实现者接口
class Implementor:
    def operation(self):
        pass


# 具体实现A
class ConcreteImplementorA(Implementor):
    def operation(self):
        return "具体实现A的工作"


# 具体实现B
class ConcreteImplementorB(Implementor):
    def operation(self):
        return "具体实现B的工作"


# 抽象类
class Abstraction:
    def __init__(self, implementor):
        self._implementor = implementor

    def operation(self):
        return self._implementor.operation()


# 细化抽象类
class RefinedAbstraction(Abstraction):
    def operation(self):
        result = super().operation()
        return "细化抽象处理结果: " + result


if __name__ == '__main__':
    implementor_a = ConcreteImplementorA()
    abstraction = Abstraction(implementor_a)
    print(abstraction.operation())

    implementor_b = ConcreteImplementorB()
    refined_abstraction = RefinedAbstraction(implementor_b)
    print(refined_abstraction.operation())
