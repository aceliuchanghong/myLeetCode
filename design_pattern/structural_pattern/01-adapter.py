"""
适配器模式
"""


# 旧系统中的类，使用英制单位
class OldMeasurementSystem:
    def get_length_in_feet(self):
        return 5  # 假设长度是5英尺

    def get_height_in_inches(self):
        return 30  # 假设高度是30英寸


# 新系统中的类，使用公制单位
class NewMeasurementSystem:
    def get_length_in_meters(self):
        raise NotImplementedError("This method should be implemented by an adapter")

    def get_height_in_centimeters(self):
        raise NotImplementedError("This method should be implemented by an adapter")


# 适配器类，将英制单位转换为公制单位
class MeasurementAdapter(NewMeasurementSystem):
    def __init__(self, old_system):
        self.old_system = old_system

    def get_length_in_meters(self):
        feet = self.old_system.get_length_in_feet()
        return feet * 0.3048  # 1英尺 = 0.3048米

    def get_height_in_centimeters(self):
        inches = self.old_system.get_height_in_inches()
        return inches * 2.54  # 1英寸 = 2.54厘米


# 客户端代码
if __name__ == "__main__":
    old_system = OldMeasurementSystem()
    adapter = MeasurementAdapter(old_system)

    print(f"Length in meters: {adapter.get_length_in_meters()}")
    print(f"Height in centimeters: {adapter.get_height_in_centimeters()}")
