package practice;

import java.util.Arrays;

public class ArrayPractice {
	
	public static void main(String[] args) {
		String[] array = new String[10];
		
		for(int i=0; i<array.length; i++)
			array[i] = Integer.toString(i);
		
		System.out.println("\n" + Arrays.toString(array));
		
	}
}
