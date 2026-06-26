class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stacker = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                right = stacker.pop()
                left = stacker.pop()
                if token == '+':
                    stacker.append(int(right)+int(left))
                elif token == '-':
                    stacker.append(int(left)-int(right))
                elif token == '*':
                    stacker.append(int(right)*int(left))
                elif token == '/':
                    stacker.append(int(int(left)/int(right)))
            else:
                stacker.append(token)
        return int(stacker.pop())


        