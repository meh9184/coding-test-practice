public class UserInput {
    
    public static class TextInput {
        static String value = "";
    	public void add(char c) { this.value += c; }
    	public String getValue() { return this.value; }
    }

    public static class NumericInput extends TextInput{
    	@Override
    	public void add(char c) {
    		if( 48<=c && c<=57 ) this.value += c;
    	}
    }

    public static void main(String[] args) {
    	TextInput input = new NumericInput();
        input.add('1');
        input.add('a');
        input.add('0');
        System.out.println(input.getValue());
    }
}