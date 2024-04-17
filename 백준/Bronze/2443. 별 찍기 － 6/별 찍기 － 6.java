import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Scanner;

class Main {
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = scanner.nextInt();
        String star = "*";
        String t = " ";
        int temp = 0;
        for(int i = (n*2)-1; i > 0; i -= 2){
            for (int j = 0; j<temp ; j++) {
                bw.write(t);
            }
            for (int j = 0; j<i ; j++) {
                bw.write(star);
            }
            temp++;
            bw.newLine();
        }
        bw.flush();
        bw.close();
    }
}
