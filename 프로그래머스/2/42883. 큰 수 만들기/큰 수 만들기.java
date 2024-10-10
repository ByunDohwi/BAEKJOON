/*
1. int 배열로 만들어서 내림차순 정렬해서 k만큼 자르기.
2. HashMap을 사용해서 높은값과 갯수를 key value로 등록
3. map 사용해서 number을 보며 잘해보기
*/
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Stack;
import java.util.stream.Stream;

class Solution {

    public String solution(String number, int k) {
        String answer= "";
        int[] arr1 = Stream.of(number.split("")).mapToInt(Integer::parseInt).toArray();
        Stack<Integer> stack = new Stack<Integer>();
        stack.add(10);
        for(int i = 0; i<arr1.length; i++){
            while(stack.peek() < arr1[i]&&k!=0){
                stack.pop();
                k--;
            }
            stack.add(arr1[i]);

        }
        for (int i = arr1.length-k; i < arr1.length; i++) {
            stack.pop();
        }

        while(stack.peek()!=10){
            answer = stack.pop()+answer;
        }
            return answer;
    }
}