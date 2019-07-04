public class RandomPrint {
	public static void main(String[] args) {
		
		// 0으로 채워진 4X4 배열 선언
		int[][] numbers = {
				{0, 0, 0, 0},
				{0, 0, 0, 0},
				{0, 0, 0, 0},
				{0, 0, 0, 0}
			};
		
		// 10개의 랜덤 숫자 생성하여 16개의 자리에 랜덤하게 배치
		for(int i=0; i<10; i++) {
			
			// 1~10 랜덤으로 숫자 생성
			int randomNumber = (int)(Math.random() * 10) + 1;
			
			// 0~15 랜덤으로 인덱스 생성
			int randomIndex = (int)(Math.random() * 16);
			
			// 2차원 배열의 인덱스에 맞게 row와 column계산
			int row = randomIndex/4;
			int column = randomIndex%4;
			
			// numbers 배열 안에 이미 값이 들어있다면 다시 랜덤으로 인덱스를 생성하여 삽입
			while(numbers[row][column] != 0) {
				// 0~15 랜덤으로 인덱스 생성
				randomIndex = (int)(Math.random() * 16);
				
				// 2차원 배열의 인덱스에 맞게 row와 column계산
				row = randomIndex/4;
				column = randomIndex%4;
			}
			
			// 삽입된 적이 없는 랜덤 인덱스에 랜덤으로 생성한 숫자 삽입
			numbers[row][column] = randomNumber;
			
		}
		// 랜덤하게 배치된 4X4 배열 출력
		for(int i=0; i<numbers.length; i++) {
			for(int j=0; j<numbers[i].length; j++) {
				System.out.print(numbers[i][j] + " ");
			}
			System.out.println();
		}
	}
}
