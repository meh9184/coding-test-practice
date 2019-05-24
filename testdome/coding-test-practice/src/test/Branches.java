package test;

import java.util.HashSet;
import java.util.Set;

public class Branches {
    public static int count(int[] tree) {
		// ����ũ�� ���� ����� ���� HashSet �ڷᱸ�� ���
    	Set<Integer> set = new HashSet<Integer>();
		
    	// tree ��ȸ�ϸ� ��ü ����� �θ� ��� ������ set�� ����
		for(int parentNode : tree) 
			set.add(parentNode);

		// ��Ʈ ��带 ���� (�θ��尡 -1�� ���̽�)
		set.remove(-1);
		
		// ����ũ�� ��� ���� ����
		return set.size();
    }

    public static void main(String[] args) {
        System.out.println(Branches.count(new int[] { 1, 3, 1, -1, 3 }));
    }
}