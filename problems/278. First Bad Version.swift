/*
 * The knows API is defined in the parent class VersionControl.
 *     func isBadVersion(_ version: Int) -> Bool{}
 */
    func firstBadVersion(_ n: Int) -> Int {
        var left = 1
        var right = n
        var mid:Int
        var rightGuess: Bool
        var leftGuess: Bool
        
        while true{
            mid = (left+right)/2
            rightGuess = isBadVersion(mid+1)
            leftGuess = isBadVersion(mid)      
            
            if !leftGuess && rightGuess{
                return mid + 1
            }else{
                if leftGuess {
                    right = mid - 1
                }else{
                    left = mid + 1
                }
            }
        }
