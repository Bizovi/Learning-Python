import socket

# Lambda and friends in functional programming: useful because they are callable
# Lambda uses callable, also used extensively in decorators
# But this is also quite dangerous

class Resolver:
    """DNS Caching resolver version: Class implementing callable methods"""
    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        """Such that the instance can be called as any other function"""
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache

    def clear(self):
        self._cache.clear()

    def has_host(self, host):
        return host in self._cache


if __name__ == '__main__':
    resolve = Resolver()
    print(resolve('sixty-north.com')) # resolve.__call__()
    print(resolve('pluralsight.com'))
    print(resolve.__dict__)
    print('Object resolve callable? ', callable(resolve))
