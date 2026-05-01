import operator
class Solution: # shorter code
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+':operator.add,"-":operator.sub,"*":operator.mul,"/":lambda a, b: int(a/b)}
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(ops[t](n1,n2))
        return stack[0]