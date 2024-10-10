import java.util.Arrays;

class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0,number = 0;
        Arrays.sort(d);
        for(int num:d){
            number += num;
            if(number>budget){
                break;
            }
            answer++;
            System.out.println(num+","+budget+","+number);
        }
        return answer;
    }
}