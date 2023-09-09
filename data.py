



class Data:
    @classmethod
    def from_dict(cls):
        ...

    def to_dict(self):
        ...


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

