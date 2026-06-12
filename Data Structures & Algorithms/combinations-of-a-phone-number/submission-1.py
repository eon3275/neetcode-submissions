class Solution: #iteration
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = ['']
        digitTochar = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
                       '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        for d in digits:
            curr = []
            for c in digitTochar[d]:
                for r in res:
                    curr.append(r+c)
            res = curr
        return res