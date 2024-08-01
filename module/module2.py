class Module2:
    def __init__(self, *nums) -> None:
        self.nums = nums
    
    def sum_numbers(self) -> int:
        total = 0
        for num in self.nums:
            total += num
        return total