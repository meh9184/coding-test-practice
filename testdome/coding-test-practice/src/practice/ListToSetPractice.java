package practice;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;


public class ListToSetPractice {
	
	public static void main(String[] args) {
		List<String> list = new ArrayList<String>();
		
		// 리스트에 [1-10, 1-10] String 타입으로 원소 삽입
		for(int i=1; i<=10; i++)
			list.add( Integer.toString(i) );
		for(int i=1; i<=10; i++)
			list.add( Integer.toString(i) );
		
		Set<String> set = new HashSet<String>(list);
		
		
		System.out.println(set);
		
	}
	
	
}