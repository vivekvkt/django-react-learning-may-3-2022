class ProductFinder:
    def productExceptSelf(self, nums):
        output = [1 for i in range(len(nums))]
        for i in range(1,len(output)):
            output[i] = output[i-1]*nums[i-1]
        R = 1
        for i in range(len(output)-1, -1, -1):
            output[i] = output[i]*R
            R *=nums[i]
        return output