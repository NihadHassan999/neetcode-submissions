class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       freq_dict = dict()
       # count the freq
       for item in nums:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
       buckets = [[] for _ in range(len(nums)+1)]
       for num, freq in freq_dict.items():
            buckets[freq].append(num)
       result = []
       for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result