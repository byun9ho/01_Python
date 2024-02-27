#가시성


class Product(object):
    pass

class Inventory(object):
    def __init__(self):
        self.__items=[]

    def addNewItem(self,product):
        if type(product)==Product: # product로 생성된 객체가 Product 클래스인지? (is라는 것과 동일)
            self.__items.append(product)
            print('new item added')
        else:
            print('error')

    def getNumberofItems(self):
        return len(self.__items)

    def getItems(self):
        # print(self.__items)
        return self.__items

#데코레이터 @property를 사용하여 비공개필드를 직접 접근하여 사용
    @property
    def items(self):
        return self.__items

myInvent=Inventory()
myInvent.addNewItem(Product())
myInvent.addNewItem(Product())
myInvent.addNewItem(Product())

print('myInvent =',myInvent.getItems(),type(myInvent.getItems()))
print('myInventory number =',myInvent.getNumberofItems())
print('Property 사용: ',myInvent.items)



# myInvent.__items  #AttributeError: 'Inventory' object has no attribute '__items'

