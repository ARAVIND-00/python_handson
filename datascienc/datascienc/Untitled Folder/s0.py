

class Solution:
    def relativeSortArray(self, arr1, arr2):
        result=[]

        for value in arr2:

            for i in range(len(arr1)):
                if arr1[i]==value:
                    result.append(arr1[i])
                    arr1[i]=-1
        arr1.sort()


        for value in arr1:
            if value !=-1:
                  result.append(value)
        return result
                              

b=Solution()
print(b.relativeSortArray([3,1,2,2,3,3,4,5,6,7],[4,3,2,5]))

