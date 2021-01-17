class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i in range(len(nums)):
            il=i+1
            ih=len(nums)-1
            if i==0 or nums[i]!=nums[i-1]:
                while il<ih:
                    total=nums[i]+nums[il]+nums[ih]
                    if total<0:
                        il+=1
                    elif total>0:
                        ih-=1
                    else:
                        ans.append([nums[i],nums[il],nums[ih]])
                        il+=1
                        ih-=1
                        while (nums[il]==nums[il-1] and il<ih):
                            il+=1
        return ans
