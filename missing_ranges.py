class Solution:
    def findMissingRanges(self, nums, lower, upper):
        result = []
        prev = lower - 1

        for num in nums + [upper + 1]:
            if num - prev >= 2:
                if num - prev == 2:
                    result.append(str(prev + 1))
                else:
                    result.append(str(prev + 1) + "->" + str(num - 1))

            prev = num

        return result
