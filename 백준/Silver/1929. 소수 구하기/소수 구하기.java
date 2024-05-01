import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        int[] arr = new int[1000001];
        for(int i = 0; i<= b; i++)
            arr[i] = i;
        for(int i = 2; i <= b; i++){
            if(arr[i] == 0)
                continue;
            for (int j = i * 2; j <= b; j += i) {
                arr[j] = 0;
            }
        }
        for (int i = a; i <= b; i++) {
            if(arr[i]== 0 || arr[i] == 1)
                continue;
            System.out.println(i);
        }
    }
}
