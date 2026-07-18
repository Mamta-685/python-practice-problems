class Solution:
    def maxConsecutiveOnes(self,arr,n):
        counter = 0
        max_count = 0
        for i in range(n):
            if arr[i]==1:
                counter +=1
                if counter > max_count:
                    max_count = counter
            elif arr[i] == 0:
                counter = 0
        return max_count
    
sol = Solution()
arr = [1,1,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0]
n = len(arr)
print(sol.maxConsecutiveOnes(arr,n))
        
#Output: 11
