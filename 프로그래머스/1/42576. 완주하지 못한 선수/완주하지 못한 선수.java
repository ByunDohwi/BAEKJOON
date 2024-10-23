/*

* HashMap을 사용
1. 완주한 사람을 key값으로 등록 value는 null로 한다. -> HashMap은 key, value가 nullable이기 때문
2. 참여한 사람을 반복하며 key값으로 담기지 않은 사람을 return한다.

*/

import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> map = new HashMap<>();
        for (String people : completion) {
            if(map.containsKey(people)){
                map.put(people, map.get(people)+1);
            }else{
                map.put(people, 0);
            }
        }
        for (String people : participant) {
            if (!map.containsKey(people)) {
                return people;
            }
            if(map.get(people) > 0){
                map.put(people, map.get(people)-1);
            }else{
            map.remove(people);
            }
        }
        return map.entrySet().iterator().next().getKey();
    }
}
