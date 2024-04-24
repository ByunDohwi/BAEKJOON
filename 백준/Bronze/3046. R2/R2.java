import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String input = br.readLine();
        StringTokenizer inputT = new StringTokenizer(input);
        int S1 = Integer.parseInt(inputT.nextToken());
        int R = Integer.parseInt(inputT.nextToken());
        R *= 2;
        String answer = Integer.toString(R - S1);
        bw.write(answer);

        bw.flush();
        bw.close();
    }
}