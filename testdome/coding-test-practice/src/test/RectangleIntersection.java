package test;

import java.util.Scanner;

class Point{
	public int x;
	public int y;
	Point(int x, int y){
		this.x = x;
		this.y = y;
	}
}

public class RectangleIntersection {

	public static void main(String[] args) {
		int testCase;
		Point[] points = new Point[4];
		Scanner scanner = new Scanner(System.in);
				
		testCase = Integer.parseInt(scanner.next());
		for(int i=0; i<testCase; i++) {
			
			// �� 4�� �Է¹���
			for(int j=0; j<4; j++) {
				int x = Integer.parseInt(scanner.next());
				int y = Integer.parseInt(scanner.next());
				
				points[j] = new Point(x, y);
			}
			
			// �⺻ ���簢�� ����
			int area = getArea(points[0], points[1]);
			
			// ���� �κ� ���簢�� ����
			int intersection = getIntersection(points);
			
			// �ȵ��� �κ� ���簢�� ����
			System.out.println(area - intersection);
			
		}
	}
	
	public static int getArea(Point point1, Point point2) {
		int width = point2.x - point1.x;
		int height = point2.y - point1.y;
		
		return width * height;
	}
	
	public static int getIntersection(Point[] points) {

		// �� ���簢���� ��ġ�� �ʴ� ���
		if(points[1].x <= points[2].x 
		|| points[0].x >= points[3].x
		|| points[1].y <= points[2].y 
		|| points[0].y >= points[3].y)
			return 0;
		
		// �� ���簢���� ��ġ�� ���
		else {
			int x1 = Math.max(points[0].x, points[2].x);
			int y1 = Math.max(points[0].y, points[2].y);
			
			int x2 = Math.min(points[1].x, points[3].x);
			int y2 = Math.min(points[1].y, points[3].y);
			
			Point point1 = new Point(x1, y1);
			Point point2 = new Point(x2, y2);
			
			return getArea(point1, point2);	
		}
	}
}
