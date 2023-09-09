



from typing import Any


class Data:
    def __init__(self,**kwargs):
        self.load_data(kwargs)
        
    @classmethod
    def from_dict(cls, data_dict):
        instance = cls()
        instance.load_data(data_dict)
        return instance
    

    def to_dict(self):
        data_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, Data):
                data_dict[key] = value.to_dict()
            else:
                data_dict[key] = value
        return data_dict
    
    def load_data(self, data_dict):
        # if not data_dict:
        #     return
        for key, value in data_dict.items():
            if isinstance(value, dict):
                setattr(self, key, Data.from_dict(value))
            else:
                
                setattr(self, key, value)
                

    # def __getattr__(self, name):
    #     if name not in self.__dict__:
    #         return Data()
    #     return self.__dict__[name]

    # def __setattr__(self, name, value):
    #     if name not in self.data:
    #         self.data[name] = value
    #     else:
    #         self.data[name] = value
            

    def __repr__(self) -> str:
        #get all the attributes of the class and child class
        attrs = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
        return f"{self.__class__.__name__}({attrs})"
    
    def __getattr__(self, name):
        if name not in self.__dict__:
            for key, value in self.__dict__.items():
                if isinstance(value, Data):
                    return getattr(value, name)
                elif not isinstance(value, Data):
                    if name == key:
                        return value
                    elif not any(isinstance(value, Data) for value in self.__dict__.values()):
                        setattr(self, name, 100)
                        return self.__dict__[name]
        else:
            return self.__dict__[name]

    def __dir__(self):
        # Get a list of attribute names and nested attribute names for autocomplete
        def get_attr_names(data_dict, prefix=""):
            attr_names = []
            for key, value in data_dict.items():
                if isinstance(value, dict):
                    attr_names.extend(get_attr_names(value, prefix + key + '.'))
                else:
                    attr_names.append(prefix + key)
            return attr_names

        return sorted(set(super().__dir__() + get_attr_names(self.to_dict())))

    
    



data = {
    "id": "1",
    "name": "first",
    "metadata": {
        "system": {
            "size": 10.7
        },
        "user": {
            "batch": 10
        }
    }
}

# load from dict
my_inst_1 = Data.from_dict(data)

# load from inputs
my_inst_2 = Data(name="my")

# reflect inner value
print(my_inst_1.size)  # should print 10

# default values
print(my_inst_1.height)  # should set a default value of 100 in metadata.system.height
print(my_inst_1.to_dict()['metadata']['system']['height'])  # should print the default value

print(my_inst_1.metadata.system.size)  # Should print 10
print(my_inst_1.metadata.user.batch)  # Should print 10

