class Model(dict):
    __metaclass__ = ModelMetaclass
    
    def __init__(self, **kw):
        super(Model, sef).__init__(**kw)

    def __getattr(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'"%key)

    def __setattr__(self, key, value):
        self[key] = value

