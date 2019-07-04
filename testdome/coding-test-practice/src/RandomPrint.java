public class RandomPrint {
	public static void main(String[] args) {
		
		// 0���� ä���� 4X4 �迭 ����
		int[][] numbers = {
				{0, 0, 0, 0},
				{0, 0, 0, 0},
				{0, 0, 0, 0},
				{0, 0, 0, 0}
			};
		
		// 10���� ���� ���� �����Ͽ� 16���� �ڸ��� �����ϰ� ��ġ
		for(int i=0; i<10; i++) {
			
			// 1~10 �������� ���� ����
			int randomNumber = (int)(Math.random() * 10) + 1;
			
			// 0~15 �������� �ε��� ����
			int randomIndex = (int)(Math.random() * 16);
			
			// 2���� �迭�� �ε����� �°� row�� column���
			int row = randomIndex/4;
			int column = randomIndex%4;
			
			// numbers �迭 �ȿ� �̹� ���� ����ִٸ� �ٽ� �������� �ε����� �����Ͽ� ����
			while(numbers[row][column] != 0) {
				// 0~15 �������� �ε��� ����
				randomIndex = (int)(Math.random() * 16);
				
				// 2���� �迭�� �ε����� �°� row�� column���
				row = randomIndex/4;
				column = randomIndex%4;
			}
			
			// ���Ե� ���� ���� ���� �ε����� �������� ������ ���� ����
			numbers[row][column] = randomNumber;
			
		}
		// �����ϰ� ��ġ�� 4X4 �迭 ���
		for(int i=0; i<numbers.length; i++) {
			for(int j=0; j<numbers[i].length; j++) {
				System.out.print(numbers[i][j] + " ");
			}
			System.out.println();
		}
	}
}
