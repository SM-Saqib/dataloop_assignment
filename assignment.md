Build a Pythonic data model class `Data` with the following requirements:

1. loads a dictionary and can save to dictionary: `to_dict`, `from_dict`
2. ability to instantiate directly from the class
3. default value: can define a default value for attributes
4. autocomplete
5. dynamic and general usability for the class (easily define new data structures)
6. ability to reflect inner value on the main level


Example:
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

# autocomplete - should complete to metadata
data.me