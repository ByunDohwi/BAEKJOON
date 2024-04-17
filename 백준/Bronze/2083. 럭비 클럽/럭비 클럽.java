import java.io.*;
import java.util.StringTokenizer;

 class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter((new OutputStreamWriter(System.out)));
        int age =1 ;
        while(true){
            String Privacy = br.readLine();
            StringTokenizer st = new StringTokenizer(Privacy);
            String name = st.nextToken();
            if(name.equals("#"))
            {
                break;
            }
            age = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
                if (age > 17 || weight >= 80) {
                    String Junior = name + " Senior";
                    bw.write(Junior);
                }else{
                    String Sinior = name + " Junior";
                    bw.write(Sinior);
                }
                bw.newLine();
            }
        bw.flush();
        bw.close();
    }
}
