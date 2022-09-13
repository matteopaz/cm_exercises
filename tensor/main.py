class Tensor:
    def __copy(self, arr):
        new = []
        for e in arr:
            new.append(e)
        return new

    def __construct_raw(self, tensor, dims):
        if dims == []:
            return tensor

        return self.__construct_raw([tensor]*dims[-1], dims[0:-1])

    def __init__(self, dimensions, fill):
        self.dim = dimensions
        self.raw = self.__construct_raw(fill, dimensions)
    
    def __get_el(self, current, coordinates):
        c = self.__copy(coordinates)
        return self.__get_el(current[c[0]], c[0:])

    def get_el(self, coordinates):
        return self.__get_el(self.raw, coordinates)

    def display(self):
        print(self.raw)
    
a = Tensor([3,3,3], 0)
a.display()
print(a.get_el([0,1,2]))