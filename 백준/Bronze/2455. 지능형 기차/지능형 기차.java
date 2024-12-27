import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int answer =-1 , people = 0;
        for(int i = 0; i < 4; i++){
            int n = sc.nextInt();
            int t = sc.nextInt();
            sc.nextLine();

            people = people + t - n;
            if(people > answer) answer = people;
        }
        System.out.println(answer);
    }
}
