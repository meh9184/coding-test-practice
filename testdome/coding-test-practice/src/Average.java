public class Average {

	public static void main(String[] args) {

		// 값을 모두 누적해놓을 변수
		int sum = 0;
		
		// 파라미터의 개수
		int length = args.length;
		
		// 파라미터로 넘어온 개수만큼 반복문 돌며 sum 변수에 값 누산
		for(int i=0; i<length; i++) {
			// 파라미터 값을 int 값으로 바꿔 sum.에 누산
			sum += Integer.parseInt(args[i]);
		}
		
		// average 계산
		double average = (float)sum / length;
		
		// average 출력
		System.out.println(average);
		
	}

}