import heapq
import typing
from dataclasses import dataclass

from util.puzzle import Puzzle

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

def get_next_state(state: State, dst: Point):
    field = [ [ i for i in j ] for j in state.field ]
    field[state.point.y][state.point.x], field[dst.y][dst.x] = field[dst.y][dst.x], field[state.point.y][state.point.x]
    combo = Puzzle(field).get_combo() * -1 # heap1は最小値が取り出されるため-1を乗算
    move_history = state.move_history + [dst]
    next_state = State(field, combo, dst, move_history)
    return next_state

def beam_search(first_state, move_number):
    field_width = len(first_state.field[0])
    field_height = len(first_state.field)
    now_states = [] # 現在の状態保存用
    heapq.heappush(now_states, first_state)
    k = 5 #ビーム幅
    comb = set()
    for _ in range(move_number):
        print(len(now_states))
        next_states = []
        for _ in range(k):
            if len(now_states) == 0: break
            state = heapq.heappop(now_states)
            comb.add(state.combo)
            if state.point.x-1 >= 0: next_states.append( get_next_state(state, Point( state.point.x-1, state.point.y )) )
            if state.point.x+1 < field_width: next_states.append( get_next_state(state, Point( state.point.x+1, state.point.y )) )
            if state.point.y-1 >= 0: next_states.append( get_next_state(state, Point( state.point.x, state.point.y-1 )) )
            if state.point.y+1 < field_height: next_states.append( get_next_state(state, Point( state.point.x, state.point.y+1 )) )
        heapq.heapify(next_states)
        now_states = next_states
    print(comb)
    return heapq.heappop(now_states)

def main():
    field = [
        [0,1,2,3,4,5,6],
        [1,2,3,4,5,6,0],
        [2,3,4,5,6,0,1],
        [3,4,5,6,0,1,2],
        [4,5,6,0,1,2,3]
    ]
    
    first_point = Point(2, 2)
    first_state = State(field, 0, first_point, [first_point])
    result = beam_search(first_state, 20)
    print(result)

if __name__ == "__main__":
    main()