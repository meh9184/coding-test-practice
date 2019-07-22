class Solution
  def solution(arr)
    
    result = 0
    
    if !is_sorted(arr, 0, arr.length-1)
      max = arr.max_by{|e| e} 
      min = arr.min_by{|e| e} 

      insertion_sort_ith(arr, )
    end


    return 0
  end

  def is_sorted(arr, i, j)
    for k in (i+1)...j
      if arr[k] > arr[k+1]
        return false
      end
    end
    
    return true
  end

  def insertion_sort_ith(arr, i)
    while true
      if i < arr.length-1 and arr[i] < arr[i+1]
        tmp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = tmp
        i+=1
      elsif i == arr.length-1
        break
      end
    
  end

end

s = Solution.new
puts s.solution([1,8,8,12,99])
