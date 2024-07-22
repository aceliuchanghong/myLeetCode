import copy


# /ˈprəʊtətʌɪp/ 样品 ==> 原型模式
class Prototype:

    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        if obj is None:
            raise ValueError(f"No object registered with name: {name}")
        """
        __dict__是一个字典（dictionary），其中键（key）是属性名或方法名，值（value）是对应的属性值或方法对象。
        """
        obj.__dict__.update(attr)
        return obj


class ConcretePrototype:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"Name: {self.name}, Value: {self.value}"


if __name__ == '__main__':
    prototype = Prototype()
    concrete_prototype = ConcretePrototype("Prototype1", 10)
    prototype.register_object("Prototype1", concrete_prototype)
    cloned_prototype = prototype.clone("Prototype1", value=20)

    print(concrete_prototype)
    print(cloned_prototype)
