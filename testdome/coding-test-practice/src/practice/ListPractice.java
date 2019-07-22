package practice;

import java.util.ArrayList;
import java.util.List;


public class ListPractice {
	
	public static void main(String[] args) {
		List<String> list = new ArrayList<String>();
		
		list.add("문은환");
		list.add("자바");
		
		System.out.print("리스트 안의 원소 : ");
		for(String str : list) {
			System.out.print(str + " ");
		}
		
		System.out.println("\n" + list);
		
	}
	
	
}
