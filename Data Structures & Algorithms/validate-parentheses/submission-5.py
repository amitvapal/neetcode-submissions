class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {')' : '(', '}' : '{', ']' : '['}
        stack = []

        for c in s:
            if c in mapper:
                if not stack or stack[-1] != mapper[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return (len(stack)==0)
            

            

        