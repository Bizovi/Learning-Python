"""
Example from refactoring guru
https://refactoring.guru/design-patterns/factory-method/python/example#lang-features
"""

from abc import ABC, abstractmethod


class Creator(ABC):
    """
    Declares factory method, which should return object of product class. 
    The subclasses usually provide an implementation of this
    """

    @abstractmethod
    def factory_method(self):
        """Can provide some default implementation of the factory method"""
        pass

    def some_operation(self) -> str:
        # Call the factory method to create a product object
        product = self.factory_method()

        # Use the product
        result = f"""Creator: The same creator's code has just worked with 
            {product.operation()}"""
        return result

class Product(ABC):
    """The Product interface declares the operations that all concrete products
    must implement.
    """

    @abstractmethod
    def operation(self) -> str:
        pass
    
"""
Concrete Products provide various implementations of the Product interface.
"""

class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""
class ConcreteCreator1(Creator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """
    def factory_method(self) -> ConcreteProduct1:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> ConcreteProduct2:
        return ConcreteProduct2()




def client_code(creator: Creator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
        f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
