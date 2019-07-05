class Solution
  def solution(words)
    
    # 최종 리턴할 값을 0으로 초기화 하고, 
    # 겹치는 쌍이 발생할때 마다 1씩 증가
    result = 0

    # 전체 단어 리스트를 순회하며 등장하는 알파벳을 a-z 순으로 맵핑
    for i in 0...words.length

      # 첫번째 아스키코드를 97로 설정 (문자 a)
      ascii = 97
      # 각 문자가 등장하는 순서대로 a-z 아스키코드를 할당하기 위해 저장공간 dict 선언
      dict = {}

      # 한 문자열을 문자별로 순회하며 a-z 문자 순서로 맵핑
      for j in 0...words[i].length

        # dict에 이미 존재하는 문자라면 앞에서 등장했다는 의미이므로 할당된 아스키값의 문자로 치환
        if dict.include? words[i][j]
          words[i][j] = dict[words[i][j]].chr
        # dict에 존재하지 않는 문자라면 처음 등장했다는 의미이므로 현재 아스키 값으로 치환한 후에 base 값을 1 증가
        else
          dict[words[i][j]] = ascii
          words[i][j] = ascii.chr
          ascii += 1
          
        end
      end
    end

    # 전체 단어 리스트로 치환된 문자열들을 순회하며 동일 구조 단어 쌍의 개수를 계산
    for i in 0...words.length
      for j in i...words.length
        if (i != j) and (words[i] == words[j])
          result += 1
        end
      end
    end

    return result
  end
end

s = Solution.new
puts s.solution(["abca","zbxz","opqr"])
