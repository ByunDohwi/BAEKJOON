
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int[] arr = new int[201];
        for(int i = 0; i<= 200; i++)
            arr[i] = i;
        for(int i = 2; i <= 200; i++){
            if(arr[i] == 0)
                continue;
            for (int j = i << 1; j <= 200; j += i) {
                arr[j] = 0;
            }
        }
        int[] arr_2 = new int[200];
        arr[1] = 0;
        arr[0] = 0;
        int num = 0;
        for (int i = 1; i <= 200; i++) {
           if(arr[i] != 0)
               arr_2[num++] = arr[i];
        }
        for (int i = 0; i < 200; i++) {
            if(a < arr_2[i]*arr_2[i+1]){
                System.out.println(arr_2[i]*arr_2[i+1]);
                return;
            }
        }

    }
}
