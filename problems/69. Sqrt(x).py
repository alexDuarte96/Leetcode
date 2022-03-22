class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        
        left = 0
        right = x
        
        while True:
            mid = (left+right)/2
            sqr = mid*mid
            distance = abs(sqr - x)
            
            if distance < 1:
                intMid = int(mid)
                integer = (intMid+1)*(intMid+1)
                
                if integer == x:
                    return int(intMid+1)
                
                return int(mid)
            
            if sqr > x:
                right = mid
            else:
                left = mid
