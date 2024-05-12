import java.io.*;

public class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bf.readLine());

        for (int i = 0; i < n; i++) {

             int ch = Integer.parseInt(bf.readLine());
             int ho = Integer.parseInt(bf.readLine());
            int[][] arr = new int[ch +1][ho+1];
            int cnt = 1;
            for(int j = 1; j <= ho; j++){
                arr[0][j] = cnt++;
            }
            for (int j = 1; j <= ch; j++) {
                for (int l = 1; l <= ho; l++) {
                    arr[j][l] = add(j-1,l,arr);
                }
            }
            System.out.println(arr[ch][ho]);
        }

    }
    public static int add(int ch,int ho, int[][] arr) {
        int answer = 0;
        for (int i = 1; i <= ho; i++) {
            answer += arr[ch][i];
        }
        return answer;
    }
}
