package practice;

import java.util.ArrayList;
import java.util.List;


public class ListPractice {
	
	public static void main(String[] args) {
		List<String> list = new ArrayList<String>();
		
		list.add("����ȯ");
		list.add("�ڹ�");
		
		System.out.print("����Ʈ ���� ���� : ");
		for(String str : list) {
			System.out.print(str + " ");
		}
		
		System.out.println("\n" + list);
		
	}
	
	
}
