class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+","-","*","/"}
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                if t=="+":
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(n2+n1)
                elif t=="-":
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(n2-n1)
                elif t=="*":
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(n2*n1)
                else:
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(int(n2/n1))
        return stack[0]