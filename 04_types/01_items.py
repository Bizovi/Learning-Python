from typing import (
	Sequence, Tuple, List,
	Callable,
	Union, Optional,
	overload,
	TypeVar,  # generic functions
	Any,
	cast,  # e.g. for json, dicts, lists (unknown shape)
)
from typing_extensions import Protocol


# Some basic examples --------------------------------------------
def square(x: int) -> int:
	return x**2


# can be unbounded, or bound of str and bytes
AnyStr = TypeVar('AnyStr', str, bytes)
# ----------------------------------------------------------------


# Photo example  -------------------------------------------------
class Photo:
	def __init__(self, width: int, height: int) -> None:
		self.width = width
		self.height = height
		self.tags: List[str] = []  # just [] would be a problem for mypy

	def get_dimension(self) -> Tuple[int, int]:
		"""static type checker would throw an error on
		Tuple[str, str]
		"""
		return self.width, self.height
# ----------------------------------------------------------------


# A more complicated example -------------------------------------
class Item:
	def __init__(self, id: int, name: str, price: float) -> None:
		self.id = id
		self.name = name
		self.price = price


# people have been putting these in docstrings for years
# but we forget to update the docstring
class Cart:
	def __init__(self, items: list = []) -> None:
		self.items = items

	def process(self, items: Sequence[Item]) -> None:
		for item in items:
			self.items.append(item.name)
# ----------------------------------------------------------------


# For multiple types  --------------------------------------------
class Foo:
	def __init__(self, id: int) -> None:
		self.id = id

#  Union[Foo, None] === Optional[Foo]
@overload  # pattern matching, purely for the type checker
def get_foo2(foo_id: None) -> None:
	pass


@overload
def get_foo2(foo_id: int) -> Foo:
	pass


def get_foo2(foo_id: Optional[int]) -> Optional[Foo]:
	"""This is pretty sad, needs more checks afterwards"""
	if foo_id is None:
		return None
	return Foo(foo_id)  # Foo(foo_id)
# ----------------------------------------------------------------


# ----------------------------------------------------------------
def concat(a: AnyStr, b: AnyStr) -> AnyStr:
	"""Both should be of the same type"""
	return a + b


# def __getattr__(self, name: str) -> Any:
# 	"""Really don't know anything about what am returning
# 	-> Escape patch #1.
# 	"""
# 	return getattr(self.wrapped, name)
# ----------------------------------------------------------------


# what about any object? ... but it might fail at runtime
# def render(obj: Any) -> str:
# 	return obj.render()
# ----------------------------------------------------------------

class Renderable(Protocol):
	"""Such that it matches protocol. e.g. a Foo() with a render method
	Structural sub-typing: has same methods and attributes (matches structure)
	"""
	def render(self) -> str:
		pass


def render(obj: Renderable) -> str:
	return obj.render()


# ----------------------------------------------------------------
def factorial(x: int) -> int:
	res = 1
	for i in range(1, x + 1):
		res *= i
	return res


def map_int_list(fn: Callable, params: List[int]) -> List[int]:
	return [fn(param) for param in params]


# ----------------------------------------------------------------


if __name__ == "__main__":
	book1 = Item(1221, "BDA3 - Gelman", 34.99)
	book2 = Item(1223, "Econometrics - Triverdi", 50.00)
	books = [book1, book2]

	my_cart = Cart()
	my_cart.process(books)
	print(my_cart.__dict__)

	# would ideally be in some kind of test suite
	# print(square(23.5), square('foo'), square(3) + 'foo')

	my_photo = Photo(width=300, height=400)
	print(my_photo.get_dimension())
	print(map_int_list(factorial, list(range(1, 10))))
