import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        char[] arr = a.toCharArray();
        int[] intArr = new int[arr.length];
        char temp = (arr[0] == '1'?'0':'1');
        int cnt = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != temp) {
                intArr[cnt++] = ((arr[i])-48);
                temp = arr[i];
            }
        }
        int k=0, l =0;
        for (int i = 0; i < cnt; i++) {
            if (intArr[i] == 1) {
                k++;
            } else {
                l++;
            }
        }
        System.out.println((Math.min(k, l)));
    }
}