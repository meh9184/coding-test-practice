class Solution
  def solution(n)

    # 0보다 같거나 작은 음수라면 0 리턴 
    if n <= 0
      return 0
    end

    # 최종 리턴할 값을 n-1로 초기화 하고, 
    # 겹치는 문자가 발생할때 마다 1씩 감소
    result = n-1
    
    # 겹치는 문자 확인하기 위해 각 자리 수의 빈도를 저장할 해쉬 bucket 선언
    bucket = {
      "0" => 0, 
      "1" => 0, 
      "2" => 0, 
      "3" => 0, 
      "4" => 0, 
      "5" => 0, 
      "6" => 0, 
      "7" => 0, 
      "8" => 0, 
      "9" => 0
    }
  
    # 1~n-1 까지 중복 digit 값 있는지 계산 시작
    for number in 1...n

      # 각 숫자마다 빈도수 값을 의미하는 bucket을 0으로 초기화
      for key in bucket.keys
        bucket[key] = 0
      end

      # 숫자를 string으로 변환
      number = number.to_s

      # 각 문자열의 자리 수를 비교하며 중복 값이 있는지 확인
      for i in 0...number.length

        # 현재 자리 수의 버킷 번호를 1 증가
        bucket[number[i]] += 1

        # 증가한 값이 2라면 중복 값이 있다는 의미이므로 전체 결과에서 1 감소하고 계속 진행
        if bucket[number[i]] == 2
          result -= 1
          next
        end
      end
    end

    # n-1 에서 중복된 케이스를 뺀 결과를 리턴
    return result
  end
end


s = Solution.new
puts s.solution(7)
