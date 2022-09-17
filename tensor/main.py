class Tensor:
    def __copy(self, arr):
        new = []
        for e in arr:
            new.append(e)
        return new

    def __construct_raw(self, tensor, dims):
        if dims == []:
            return tensor
        return self.__construct_raw([tensor]*dims[-1], dims[0:-1]) # Constructs from bottom up

    def __init__(self, dimensions, fill):
        self.dim = dimensions
        self.raw = self.__construct_raw(fill, dimensions)
    
    def __get_el(self, current, coordinates):
        if coordinates == []:
            return current
        c = self.__copy(coordinates)
        return self.__get_el(current[c[0]], c[1:])

    def get_el(self, coordinates):
        return self.__get_el(self.raw, coordinates)
    
    def __set_el(self, current, coordinates, value):
        c = self.__copy(coordinates)
        if len(c) == 1:
            current[c[0]] = value
        else:
            return self.__set_el(current[c[0]], c[1:], value)
    
    def set_el(self, coordinates, value):
        self.__set_el(self.raw, coordinates, value)
        return self

    def display(self):
        print(self.raw)
    
a = Tensor([3,3,3], 0)
a.set_el([0,1,2],1)
a.display()
print(a.get_el([0,1,2]))