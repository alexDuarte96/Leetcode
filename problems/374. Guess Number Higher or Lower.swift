/** 
 * Forward declaration of guess API.
 * @param  num -> your guess number
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0 
 * func guess(_ num: Int) -> Int 
 */

class Solution : GuessGame {
    func guessNumber(_ n: Int) -> Int {
        var left:Int = 1
        var right:Int = n
        var mid:Int
        var test:Int

        while true{
            mid = (left+right) / 2
            test = guess(mid)
        
            if test == -1 {
                right = mid - 1
            }else if test == 1{
                left = mid + 1
            }else {
                return mid
            }
        }
    }
}
