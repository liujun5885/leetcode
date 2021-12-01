class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Dont' know how to call it, just recursion?
        Time complexity: 
        """
        mapping = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], 
        '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        
        def recursion(digits):
            if len(digits) == 0:
                return []
            if len(digits) == 1:
                return mapping.get(digits[0])
            first = mapping.get(digits[0])
            second = recursion(digits[1:])
            first = self.mergeTwoList(first, second)
            return first
        return recursion(digits)
    
    def mergeTwoList(self, A: List[str], B: List[str]) -> List[str]:
        if not (A or B):
            return []
        if not (A and B):
            return A if A else B
        return [A[i] + B[j] for i in range(len(A)) for j in range(len(B))]

    def letterCombinations_iterative(self, digits: str) -> List[str]:
        """
        BFS
        Time complexity: O(3^m * 4^n)
        """
        mapping = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], 
        '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        if len(digits) == 0:
            return []
        
        queue = ['']
        for digit in digits:
            queue_len = len(queue)
            chars = mapping.get(digit)
            for _ in range(queue_len):
                curr = queue.pop(0)
                queue += [curr + char for char in chars]
        return queue
