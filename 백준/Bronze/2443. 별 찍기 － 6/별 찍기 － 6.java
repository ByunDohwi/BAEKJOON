import java.io.*;
import java.util.Scanner;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
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
        bw.flush();//남아있는 데이터를 모두 출력시킴
        bw.close();
    }
}
