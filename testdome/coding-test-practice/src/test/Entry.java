package test;

import java.util.LinkedList;
import java.util.Queue;

public class Entry {

	Queue<String> queue;
	
	public Entry() {
		queue = new LinkedList<String>();
	}
	
    public void enter(String passportNumber) {
    	queue.add(passportNumber);
		
    }

    public String leave() {
        if(queue.isEmpty())
        	return null;
        else
        	return queue.remove();
    }
    
    public static void main(String[] args) {
        Entry entry = new Entry();
        entry.enter("AB54321");
        entry.enter("UK32032");
        System.out.println(entry.leave());
        System.out.println(entry.leave());
    }
}