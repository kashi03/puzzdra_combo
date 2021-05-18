from dataclasses import dataclass
from pprint import pprint

@dataclass
class Drop:
    type: int
    delete_flag: bool = False
    search_flag: bool = False
    combo_check_hash: str = ''

class Puzzle:
    def __init__(self, f) -> None:
        # パズル盤面のコピー
        # [ ドロップ種類, 消失フラグ, 探索フラグ, コンボチェックフラグ ]
        self.field = [ [ Drop(i) for i in j ] for j in f ]
        self.field_width = len(f[0])
        self.field_height = len(f)
    
    def _next_field(self):
        def down_drop(x, y):
            if self.field[y+1][x].delete_flag:
                self.field[y][x], self.field[y+1][x] = self.field[y+1][x], self.field[y][x] # 上下入れ替え
                if y+1 < self.field_height-1: down_drop(x, y+1)
                return
            else:
                return

        for y in range(self.field_height-2, -1, -1):
            for x in range(self.field_width-1, -1, -1):
                down_drop(x, y)
        for y in range(self.field_height):
            for x in range(self.field_width):
                if self.field[y][x].delete_flag:
                    self.field[y][x] = Drop(-1)
                else:
                    self.field[y][x] = Drop(self.field[y][x].type)

    def _check_combo(self, x, y) -> bool:
        self.field[y][x]
        return True

    def _check_drop(self, x, y, drop_type, combo_check_hash):
        if drop_type != self.field[y][x].type or self.field[y][x].search_flag or self.field[y][x].type == -1:
            return
        else:
            # 探索フラグを立てる
            self.field[y][x].search_flag = True
            if x-1 >= 0 and x+1 < self.field_width:
                if self.field[y][x-1].type == drop_type and self.field[y][x+1].type == drop_type:
                    self.field[y][x].delete_flag = True
                    self.field[y][x].combo_check_hash = combo_check_hash
                    self.field[y][x-1].delete_flag = True
                    self.field[y][x-1].combo_check_hash = combo_check_hash
                    self.field[y][x+1].delete_flag = True
                    self.field[y][x+1].combo_check_hash = combo_check_hash
            if y-1 >= 0 and y+1 < self.field_height:
                if self.field[y-1][x].type == drop_type and self.field[y+1][x].type == drop_type:
                    self.field[y][x].delete_flag = True
                    self.field[y][x].combo_check_hash = combo_check_hash
                    self.field[y-1][x].delete_flag = True
                    self.field[y-1][x].combo_check_hash = combo_check_hash
                    self.field[y+1][x].delete_flag = True
                    self.field[y+1][x].combo_check_hash = combo_check_hash
            
            if x-1 >= 0: self._check_drop(x-1, y, drop_type, combo_check_hash) # 左
            if x+1 < self.field_width: self._check_drop(x+1, y, drop_type, combo_check_hash) # 右
            if y-1 >= 0: self._check_drop(x, y-1, drop_type, combo_check_hash) # 上
            if y+1 < self.field_height: self._check_drop(x, y+1, drop_type, combo_check_hash) # 下
            return

    def get_combo(self):
        combo = 0
        
        while True:
            for y, row in enumerate(self.field):
                for x, col in enumerate(row):
                    self._check_drop(x, y, col.type, f'{x}{y}')

            combo_hash = set()
            for row in self.field:
                for col in row:
                    if col.combo_check_hash != '': combo_hash.add(col.combo_check_hash)

            if len(combo_hash) == 0:
                break
            combo += len(combo_hash)
            self._next_field()

            # for i in self.field:
            #     for j in i:
            #         print(str(j.type).zfill(2), end=' ')
            #     print()
            # print()
        return combo

if __name__ == "__main__":
    field = [
        [0,2,2,3,4,5],
        [0,2,1,2,5,5],
        [3,3,3,5,5,5],
        [2,2,5,0,1,2],
        [2,5,0,1,2,3]
    ]
    puz = Puzzle(field)
    combo = puz.get_combo()
    print(combo)