from abc import ABC, abstractmethod

# Interfaz del Iterador
class Iterator(ABC):
    @abstractmethod
    def getNext(self):
        pass

    @abstractmethod
    def hasMore(self) -> bool:
        pass

# Interfaz de Colección Iterable
class IterableCollection(ABC):
    @abstractmethod
    def createIterator(self) -> Iterator:
        pass

# Implementación concreta de la colección
class ConcreteCollection(IterableCollection):
    def __init__(self):
        self._items = []

    def addItem(self, item):
        self._items.append(item)

    def getItems(self):
        return self._items

    def createIterator(self) -> Iterator:
        return ConcreteIterator(self)

# Implementación concreta del iterador
class ConcreteIterator(Iterator):
    def __init__(self, collection: ConcreteCollection):
        self._collection = collection
        self._position = 0

    def getNext(self):
        if self.hasMore():
            item = self._collection.getItems()[self._position]
            self._position += 1
            return item
        return None

    def hasMore(self) -> bool:
        return self._position < len(self._collection.getItems())

# Cliente que usa el iterador
class Client:
    def __init__(self, collection: IterableCollection):
        self._iterator = collection.createIterator()

    def showItems(self):
        while self._iterator.hasMore():
            print(self._iterator.getNext())

# Ejemplo de uso
if __name__ == "__main__":
    collection = ConcreteCollection()
    collection.addItem("Elemento 1")
    collection.addItem("Elemento 2")
    collection.addItem("Elemento 3")

    cliente = Client(collection)
    cliente.showItems()
