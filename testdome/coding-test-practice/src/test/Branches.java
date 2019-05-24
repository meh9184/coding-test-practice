package test;

import java.util.HashSet;
import java.util.Set;

public class Branches {
    public static int count(int[] tree) {
		// 유니크한 값을 남기기 위해 HashSet 자료구조 사용
    	Set<Integer> set = new HashSet<Integer>();
		
    	// tree 순회하며 전체 노드의 부모 노드 정보를 set에 삽입
		for(int parentNode : tree) 
			set.add(parentNode);

		// 루트 노드를 제거 (부모노드가 -1인 케이스)
		set.remove(-1);
		
		// 유니크한 노드 개수 리턴
		return set.size();
    }

    public static void main(String[] args) {
        System.out.println(Branches.count(new int[] { 1, 3, 1, -1, 3 }));
    }
}