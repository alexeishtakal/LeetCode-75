class Solution:
    def backtrack(self, combination, next_digits):
        if not next_digits:
            self.res.append(combination)
            return

        for letter in self.map[next_digits[0]]:
            self.backtrack(combination + letter, next_digits[1:])

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        self.res = []
        self.backtrack("", digits)
        return self.res
