class AnyClass:

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        attrs = ["%s=%s" % (k, v) for (k, v) in self.__dict__.items()]
        classname = self.__class__.__name__
        return "%s: %s" % (classname, " ".join(attrs))

    def anyParas(self, *par):
        pars_list = []
        for e in par:
            pars_list.append(str(e))
        print(' '.join(pars_list))


sample = AnyClass(name = "Nam", age = 18)
sample.anyParas(1,2,3,4,5,7,'d', 'adf', (1,2), [12,4535, 'adf'], {"adf":1231})
