/*
return
배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들
1. for문을 돌며 arr배열을 탐색한다. 
2. lastNum 변수에 최근에 저장한 원소를 넣는다. 
3. if문을 통해 lastNum과 같은 값의 원소가 들어오면 arr에 넣지 않는다. 

**/

import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        LinkedList<Integer> answer = new LinkedList<>();
        int lastNum = -1;
        int idx = 0;
        for(int num: arr){
            if(lastNum != num){
                lastNum = num;
                answer.add(num);
            }
        }
        Integer[] resultArr = answer.toArray(new Integer[0]);
        return Arrays.stream(resultArr).mapToInt(Integer::intValue).toArray();
    }

}