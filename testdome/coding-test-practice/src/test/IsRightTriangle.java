package test;

import java.util.Scanner;

public class IsRightTriangle {

	public static void main(String[] args) {
		int testCase;
		Scanner scanner = new Scanner(System.in);
				
		testCase = Integer.parseInt(scanner.next());
		for(int i=0; i<testCase; i++) {
			int a = Integer.parseInt(scanner.next());
			int b = Integer.parseInt(scanner.next());
			int c = Integer.parseInt(scanner.next());

			System.out.print("Scenario " + i + ":");

			if(a*a + b*b == c*c)
				System.out.println("yes\n");
			else
				System.out.println("no\n");
			
		}
	}
	

}
