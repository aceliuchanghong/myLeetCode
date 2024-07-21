class Resource:
    def __init__(self, name):
        self.name = name

    def use(self):
        print(f"Using resource: {self.name}")


class ResourcePool:
    def __init__(self, size):
        self._pool = [Resource(f"Resource-{i}") for i in range(size)]

    def acquire(self):
        if self._pool:
            return self._pool.pop()
        else:
            raise Exception("No resources available in the pool")

    def release(self, resource):
        self._pool.append(resource)


class Client:
    def __init__(self, resource_pool):
        self.resource_pool = resource_pool
        self.resource = None

    def get_resource(self):
        self.resource = self.resource_pool.acquire()
        return self.resource

    def use_resource(self):
        if self.resource:
            self.resource.use()
        else:
            print("No resource acquired yet.")

    def release_resource(self):
        if self.resource:
            self.resource_pool.release(self.resource)
            self.resource = None
        else:
            print("No resource to release.")


if __name__ == '__main__':
    resource_pool = ResourcePool(3)
    client = Client(resource_pool)

    # 获取资源
    resource = client.get_resource()
    client.use_resource()

    # 释放资源
    client.release_resource()
    client.use_resource()

    # 再次获取资源
    resource2 = client.get_resource()
    client.use_resource()

    resource1 = client.get_resource()
    client.use_resource()

    resource0 = client.get_resource()
    client.use_resource()

