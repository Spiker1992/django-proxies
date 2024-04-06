class Mapper:
    state = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Mapper, cls).__new__(cls)
        return cls.instance