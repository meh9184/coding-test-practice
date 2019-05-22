import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.zip.ZipEntry;

public class MergeNames {
    
    public static String[] uniqueNames(String[] names1, String[] names2) {
    	    	
    	String[] concat = new String[names1.length + names2.length];
    	
    	int idx = 0;
    	for(String name : names1) concat[idx++] = name;
    	for(String name : names2) concat[idx++] = name;
    	
    	Set<String> resultSet = new HashSet<String>(Arrays.asList(concat));
    	String[] result = resultSet.toArray(new String[resultSet.size()]);

        return result;
    }
    
    public static void main(String[] args) {
        String[] names1 = new String[] {"Ava", "Emma", "Olivia"};
        String[] names2 = new String[] {"Olivia", "Sophia", "Emma"};
        
        uniqueNames(names1, names2);
        System.out.println(String.join(", ", MergeNames.uniqueNames(names1, names2))); // should print Ava, Emma, Olivia, Sophia
    }
}