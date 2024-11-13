import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int N = in.nextInt();

        Long[] DP = new Long[N + 1];
        DP[1] = 1L;
        if(N>=2){
            DP[2] = 2L;
        }
        if(N>=3){
            DP[3] = 3L;
        }

        for (int i = 4; i <= N; i++) {
            DP[i] = (DP[i-1]+DP[i-2])%10007;
        }

        System.out.println((DP[N]));

    }

}