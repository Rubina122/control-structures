from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def draw(self):
        pass
    def explain(self):
        print('This is a Shaape Object')
        print(isinstance(self,shape))


class circle(shape):
    def drawing(self):
        print('Drawing Circle')

class triangle(shape):
    def draw(self):
        print('Drawing Triangle')

class square(shape):
    def draw(self):
        print('Drawing a square')


x=circle()
print(x)
x.draw()
y=triangle()
y.draw()
z=square()
z.draw()

z.explain()
y.explain()
x.explain()