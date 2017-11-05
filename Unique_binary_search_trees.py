class Solution2:
    # @return an integer
    def numTrees(self, n):
        counts = [1, 1]
        for i in xrange(2, n + 1):
            count = 0
            for j in xrange(i):
                count += counts[j] * counts[i - j - 1]
            counts.append(count)
        return counts[-1]
    
if __name__ == "__main__":
    print Solution().numTrees(3)
