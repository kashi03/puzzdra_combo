import heapq
import typing
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

@dataclass
class State():
    field: typing.List[typing.List[int]]
    combo: int
    point: Point
    move_history: typing.List[Point]

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

def move_drop(f, src_point: typing.Tuple, dst_pint: typing.Tuple):
    field = [ [ i for i in j ] for j in f ]
    field[src_point[1]]

def beam_search(first_state, move_number):
    now_states = [] # 現在の状態保存用
    heapq.heappush(now_states, first_state)
    k = 1000 #ビーム幅
    
    for _ in range(move_number):
        next_states = []
        for _ in range(k):
            state = heapq.heappop(now_states)
            

def main():
    field = [
        [0,1,2,3,4,5,6],
        [1,2,3,4,5,6,0],
        [2,3,4,5,6,0,1],
        [3,4,5,6,0,1,2],
        [4,5,6,0,1,2,3]
    ]
    
    first_point = Point(0, 0)
    first_state = State(field, 0, first_point, [first_point])
    beam_search(first_state, 100)

if __name__ == "__main__":
    main()