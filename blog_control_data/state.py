
class Mapper:
    state = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Mapper, cls).__new__(cls)
        return cls.instance
    
    @classmethod
    def resolve_proxy_status(cls, key):
        reversed = {v: k for k, v in cls.state.items()}

        return reversed.get(key)
