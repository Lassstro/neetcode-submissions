class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [[] for _ in range(9)]
        box_1 = []
        box_2 = []
        box_3 = []
        for row in range(9):
            row_list = []
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                cols[col].append(val)
                row_list.append(val)                 
                order_box = col//3
                if order_box == 0:
                    box_1.append(val)
                if order_box == 1:
                    box_2.append(val)
                if order_box == 2:
                    box_3.append(val)
            if len(row_list) != len(set(row_list)):
                return False
            if (row+1)%3 == 0:
                if len(box_1) != len(set(box_1)):
                    return False
                if len(box_2) != len(set(box_2)):
                    return False
                if len(box_3) != len(set(box_3)):
                    return False
                box_1 = []
                box_2 = []
                box_3 = []
        for col in cols:
            if len(col) != len(set(col)):
                return False
        return True

