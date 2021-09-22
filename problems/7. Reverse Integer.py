class Solution:
    def reverse(self, x: int) -> int:

        
        asList = str(abs(x))
        newInt = 0
        power = 1
        
        flip = False
        if x < 0:
          flip = True 
        
        for digits in asList:
          newInt += int(digits) * power
          power *= 10
        
        if flip:
          newInt *= -1
          
        if newInt > 2**31 or newInt < -2**31:
          return 0
        
        return newInt
