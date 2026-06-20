class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(len(board)):
            for c in range(len(board[r])):
                val = board[r][c]
                if val == ".":
                    continue

                box = (r//3) * 3 + (c//3)

                if val in rows[r] or val in cols[c] or val in boxes[box]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                boxes[box].add(val)

        return True
                

        