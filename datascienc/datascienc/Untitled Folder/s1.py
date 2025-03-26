class solution():
    def twoSum(self,nums,target):
        
        hashmap={}
        for i in range (len(nums)):
            hashmap[nums[i]]=i
            
        for j in range (len(nums)):
            complement= target-nums[j]
            print(hashmap)
            print(complement)

            if complement in hashmap and hashmap[complement]!=j:

                return[j,hashmap[complement]]

          

        
    
      
        




b= solution()
print(b.twoSum([2,7,11,15,13,0],13))