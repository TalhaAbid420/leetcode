class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count = 0
        hash_set = set()
        
        for i in range(len(jewels)):
            hash_set.add(jewels[i])

        for j in range(len(stones)):
            if stones[j] in hash_set:
                count += 1
        
        return count