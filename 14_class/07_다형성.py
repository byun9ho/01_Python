#다형성


class Animal:
    def __init__(self,name):
        self.name=name

    def talk(self):
        raise NotImplementedError('Subclass must implement abstract method')
    #상속을 위한 목적으로 틀만 만들어 놓는 것
class Cat(Animal):
    def talk(self):
        return 'Meow!'

class Dog(Animal):
    def talk(self):
        return 'woof woof!'

# talk라는 메소드를 고양이와 강아지는 다르게 적용 - 다용성(polymorphism)

animals=[Cat('Missy'),Cat('Mr.Mistoffelees'),Dog('zion')]

for animal in animals:
    print(animal.name+': '+ animal.talk())