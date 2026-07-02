class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in nums:
            if nums.count(0) > 1:
                output = [0 for x in nums]    

            else: # only one 0
                product = 1

                for num in nums:
                    if num != 0:
                        product *= num

                output = []
            
                for num in nums:
                    if num == 0:
                        output.append(int(product))
                    else:
                        output.append(0)

        # no 0 in nums
        # calculate product of all nums 
        # builtin: math.prod()
        else:
            product = 1

            for num in nums:
                product *= num 

            # for each num in nums -> divide by num, put in new array
            output = []

            for num in nums:
                output.append(int(product/num))

        return output

        
        