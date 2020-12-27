from typing import TypeVar, Generic, List
T = TypeVar("T")


class Stack(Generic[T]):

    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


num_discs = 4
tower_a, tower_b, tower_c = Stack(), Stack(), Stack()
for i in range(1, num_discs + 1):
    tower_a.push(i)


def hanoi(begin, end, temp, n: int) -> None:
    if n == 1:
        end.push(begin.pop())
    else:
        print(f"1: hanoi({begin}, {temp}, {end}, {n - 1})")
        hanoi(begin, temp, end, n - 1)
        print("1:", begin, temp, end, "\n")

        print(f"2: hanoi({begin}, {end}, {temp}, 1)")
        hanoi(begin, end, temp, 1)
        print("2:",begin, temp, end, "\n")

        print(f"3: hanoi({temp}, {end}, {begin}, {n - 1})")
        hanoi(temp, end, begin, n - 1)
        print("3:", begin, temp, end, "\n")


if __name__ == "__main__":
    hanoi(tower_a, tower_c, tower_b, num_discs)
    print(tower_a)
    print(tower_b)
    print(tower_c)