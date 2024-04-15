import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        int temp = 0;
        for(int i = (n*2)-1; i > 0; i -= 2){
            for (int j = 0; j<temp ; j++) {
                System.out.printf(" ");
            }
            for (int j = 0; j<i ; j++) {
                System.out.printf("*");
            }
            temp++;
            System.out.println("");
        }
    }
}
