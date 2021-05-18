import heapq
import typing
from dataclasses import dataclass

@dataclass
class State():
    field: typing.List[typing.List[int]]
    combo: int
    point: typing.Tuple[int, int]

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

def beam_search(first_state, move_number):
    now_states = [] # 現在の状態保存用
    heapq.heappush(now_states, first_state)
    k = 1000 #ビーム幅
    
    for _ in range(move_number):
        next_states = []
        for state in now_states:
            pass

def main():
    field = [
        [0,1,2,3,4,5,6],
        [1,2,3,4,5,6,0],
        [2,3,4,5,6,0,1],
        [3,4,5,6,0,1,2],
        [4,5,6,0,1,2,3]
    ]
    
    first_state = State(field, 0, (0, 0))
    beam_search(first_state, 100)

if __name__ == "__main__":
    main()