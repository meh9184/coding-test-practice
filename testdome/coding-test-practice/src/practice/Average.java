package practice;

public class Average {

	public static void main(String[] args) {

		// ���� ��� �����س��� ����
		int sum = 0;
		
		// �Ķ������ ����
		int length = args.length;
		
		// �Ķ���ͷ� �Ѿ�� ������ŭ �ݺ��� ���� sum ������ �� ����
		for(int i=0; i<length; i++) {
			// �Ķ���� ���� int ������ �ٲ� sum.�� ����
			sum += Integer.parseInt(args[i]);
		}
		
		// average ���
		double average = sum / length;
		
		System.out.println(average);
		
	}

}