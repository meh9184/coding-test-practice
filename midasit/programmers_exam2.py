class Solution
    def knapsack(w, v, k)
        n = w.length
        dp = Array.new(n+1){Array.new(k+1) { 0 }}

        for i in 1...n+1
            for j in 1...k+1

                if j < w[i-1]
                    dp[i][j] = dp[i-1][j]
                else
                    dp[i][j] = [
                        dp[i-1][j],
                        v[i-1] + dp[i-1][j-w[i-1]]
                    ].max_by{|e| e}    
                end
            end
        end

        print_dp(dp, n, k)

        return dp[-1][-1]
    end

    def print_dp(dp, n, k)
        for i in 0...n+1
            for j in 0...k+1
                print '%4d'%dp[i][j]
            end
            puts
        end
    end
end

# w = [10,20,30]
# v = [60,100,120]
# k = 50

w = [5, 4, 6, 3]
v = [10, 40, 30, 50]
k = 10

s = Solution.new
puts s.knapsack(w, v, k)