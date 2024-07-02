import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        HashMap<String , String > map = new HashMap<>();
        int numD = sc.nextInt();
        int numB = sc.nextInt();
        sc.nextLine();
        LinkedList<String> list = new LinkedList<>();

        for(int i = 0; i < numD; i++){
            String str = sc.nextLine();
            map.put(str, str);
        }
        for (int i = 0; i < numB; i++) {
            String str = sc.nextLine();
            if(map.containsKey(str)){
                list.push(str);
            }
        }
        Collections.sort(list);
        System.out.println(list.size());
        for(int i = 0; i< list.size(); i++){
            System.out.println(list.get(i));
        }

    }
}
