package test;

public class Palindrome {
    public static boolean isPalindrome(String word) {
    	
    	int length = word.length();
    	word = word.toLowerCase();
    	
    	for(int i=0; i<length/2; i++) {
    		if(word.charAt( i ) != word.charAt( (length-1) - i ) )
    			return false;
    	}
    
    	return true;
    }
    
    public static void main(String[] args) {
        System.out.println(Palindrome.isPalindrome("Deleveled"));
    }
}