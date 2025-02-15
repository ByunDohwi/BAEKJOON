import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] DP = new int[N + 1];
        int[] nums = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            nums[i] = sc.nextInt();
        }

        DP[1] = 1;

        for(int i = 2; i <= N; i++) {
            int max = 0;
            for(int j = 1; j < N; j++) {
                if(nums[j] < nums[i] && DP[j] > max)
                    max = DP[j];
            }
            DP[i] = max+1;
        }
        int max = 0;
        for(int i = 1; i <= N; i++) {
            if(DP[i] > max)
                max = DP[i];
        }

        System.out.println(max);
    }

}