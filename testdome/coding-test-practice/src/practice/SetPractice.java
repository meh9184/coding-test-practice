package practice;

import java.util.ArrayList;
import java.util.List;
import java.util.HashSet;
import java.util.Set;

public class SetPractice {
	
	public static void main(String[] args) {
		Set<String> set = new HashSet<String>();
		
		set.add("apple");
		set.add("ball");
		set.add("egle");
		set.add("dog");
		set.add("banana");
		
		System.out.print("셋 안의 원소 : ");
		for(String str : set) {
			System.out.print(str + " ");
		}
		
		System.out.println("\n" + set);
		
	}
	
	
}