class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = defaultdict(int)
        for num in nums:
            result[num] += 1
        
        return [key for key, _ in sorted(result.items(), key=lambda x: x[1], reverse=True)][:k]

        