"""
适配器模式和代理模式在实现上有些相似，它们都涉及到了一个类封装另一个类的接口，但是它们解决的问题和设计意图是不同的
它们的目标不同。适配器模式的目的是适配不同接口，而代理模式是为了控制和扩展对某个对象的功能。
"""


# 实际对象类
class RealSubject:
    def request(self):
        print("RealSubject: Handling request.")


# 代理类
class Proxy:
    def __init__(self):
        self._real_subject = None

    def request(self):
        if self.check_access():
            if not self._real_subject:
                self._real_subject = RealSubject()
            self.log_access()
            self._real_subject.request()

    def check_access(self):
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self):
        print("Proxy: Logging the time of request.")


# 客户端代码
def client_code(subject):
    subject.request()


if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("\nClient: Executing the same client code with a proxy:")
    proxy = Proxy()
    client_code(proxy)
