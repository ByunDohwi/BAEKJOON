import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int N = in.nextInt();

        int[] DP = new int[N + 1];
        int[] arr = new int[N + 1];


        for (int i = 1; i <= N; i++) {
            arr[i] =in.nextInt();
        }

        DP[1] = arr[1];

        if (N >= 2) {
            DP[2] = arr[1] + arr[2];
        }

        for (int i = 3; i <= N; i++) {
            DP[i] = Math.max(DP[i - 2] , DP[i - 3] + arr[i - 1]) + arr[i];
        }

        System.out.println(DP[N]);

    }

}