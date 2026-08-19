class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        n = len(numbers)

        for i in range(n):
            comp = target - numbers[i]
            if mp[comp]:
                return [mp[comp], i+1]
            mp[numbers[i]] = i + 1
        return []

        '''
        l, r = 0, len(numbers) - 1

        while (l < r):
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l+1, r+1]

        return []
        '''