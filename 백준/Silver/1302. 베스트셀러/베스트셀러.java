import java.lang.reflect.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        TreeMap<String, Integer> map = new TreeMap<>();
        int n = sc.nextInt();
        sc.nextLine();
        int max = 0;
        String string = null;
        for (int i = 0; i < n; i++) {
            String st = sc.nextLine();
            if(map.containsKey(st)){
                map.put(st, map.get(st) + 1);
            }else{
                map.put(st, 1);
            }
            if(map.get(st)>max){
                max = map.get(st);
                string = st;
            }
            else if(map.get(st) == max){
                String[] sl = {st, string};
                Arrays.sort(sl);
                string = sl[0];
            }
        }
        System.out.println(string);
    }
}
