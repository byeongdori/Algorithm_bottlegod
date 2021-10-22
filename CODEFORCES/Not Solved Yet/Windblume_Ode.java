import java.util.Scanner;

public class Windblume_Ode {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        int testcase = input.nextInt();

        for (int i = 0; i < testcase; i++) {
            // 인풋 받아서 배열에 저장하는 과정
            int size = input.nextInt();
            int arr[] = new int[size];
            for (int j = 0; j < size; j++) {
                arr[j] = input.nextInt();
            }

            // 최대 부분집합 계산하기

        }

        input.close();
    }
}
