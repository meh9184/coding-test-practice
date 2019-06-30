package test;
import java.util.*;
import java.text.SimpleDateFormat;

public class MovieNight {
    public static Boolean canViewAll(ArrayList<Movie> movies) {

    	List<String> yearMonthDate = new LinkedList<String>();
    	
//    	for(Movie movie : movies) {
//    		String tmp = Integer.toString(movie.getStart().getYear())
//    				+ movie.getStart().getMonth().toString
//    				+ movie.getStart().getDate().toString;
//    		
//    		yearMonthDate.add(tmp);
//        	
//        }
    	
    	
    	return true;
    }

    public static void main(String[] args) throws Exception {
        SimpleDateFormat sdf = new SimpleDateFormat("y-M-d H:m");

        ArrayList<Movie> movies = new ArrayList<Movie>();
        movies.add(new Movie(sdf.parse("2015-01-01 20:00"), sdf.parse("2015-01-01 21:30")));
        movies.add(new Movie(sdf.parse("2015-01-01 23:10"), sdf.parse("2015-01-01 23:30")));
        movies.add(new Movie(sdf.parse("2015-01-01 21:30"), sdf.parse("2015-01-01 23:00")));

        System.out.println(MovieNight.canViewAll(movies));
    }
}

class Movie {
    private Date start, end;
    
    public Movie(Date start, Date end) {
        this.start = start;
        this.end = end;
    }
    
    public Date getStart() {
        return this.start;
    }
    
    public Date getEnd() {
        return this.end;
    } 
}