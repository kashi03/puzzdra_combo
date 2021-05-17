import heapq
import typing
from dataclasses import dataclass, field

@dataclass
class State():
    field: typing.List[typing.List[int]]
    combo: int
    point: typing.Tuple[int, int]
    
    def __init__(self, combo) -> None:
        self.combo = combo
    
    def __eq__(self, o) -> bool:
        return self.combo == o.combo

    def __lt__(self, o) -> bool:
        return self.combo < o.combo

    def __le__(self, o) -> bool:
        return self.combo <= o.combo

    def __gt__(self, o) -> bool:
        return self.combo > o.combo

    def __ge__(self, o) -> bool:
        return self.combo >= o.combo

def max_commbo(nums):
    pass


def main():
    pass
if __name__ == "__main__":
    main()