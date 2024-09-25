import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;

class Solution {
    public int solution(int[] picks, String[] minerals) {
        HashMap<String, Integer> map = new HashMap<>();
        int answer = 0;
        int[] arr = new int[(picks[0]+picks[1]+picks[2])<minerals.length/5+1?(picks[0]+picks[1]+picks[2]):minerals.length/5+1];

        map.put("diamond", 25);
        map.put("iron", 5);
        map.put("stone", 1);

        for(int i = 0; i < minerals.length && i < (picks[0]+picks[1]+picks[2])*5; i++){
            arr[i/5] += map.get(minerals[i])*10;
            arr[i/5]++;
        }

        Arrays.sort(arr);
        Integer[] arr3 = Arrays.stream(arr).boxed().toArray(Integer[]::new);
        Arrays.sort(arr3, Collections.reverseOrder());

        for (int score : arr3) {
            int num = score%10;
            score /= 10;
            if(picks[0] > 0){
                answer += num;
                picks[0]--;
            } else if (picks[1] > 0) {
                int temp = 0;
                if(num!=5 || score != 25){
                    temp = score/25;
                }
                answer += (temp*5) + (num-temp);
                picks[1]--;
            }else {
                answer += score;
                picks[2]--;
            }
        }

        return answer;
    }
}