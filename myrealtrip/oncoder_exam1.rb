class Solution
    def solution(n)
        su1 = 0
        su2 = 1
        result = su1 + su2

        if n == 0
            return su1
        elsif n == 1
            return su2
        elsif n == 2
            return result
        else
            for i in 0...n-2
                su1 = su2
                su2 = result
                result = su1 + su2
            end
        end

        return result
    end
end

s = Solution.new
puts s.solution(4)
