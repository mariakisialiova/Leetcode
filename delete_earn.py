class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        count = collections.Counter(nums)
        prev_num = None
        not_deleting, taken = 0,0
        for num in sorted(count):
            if num-1 != prev_num:
                not_deleting, taken = max(not_deleting, taken), count[num] * num + max(not_deleting, taken)
            else:
                not_deleting, taken = max(not_deleting, taken ), count[num] * num + not_deleting
            prev_num = num
        return max(not_deleting, taken)
