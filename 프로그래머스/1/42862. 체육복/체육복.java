/*
1. lost학생들이 번호를 map으로 등록하기
2. reserve학생들을 돌면서 자기번호-1의 학생이 map에 등록되어 있다면 체육복 빌려주기
2-1. 근데 자기도 map에 등록되어 있으면 자기가 입기
3. 반환하기
*/
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;

        Arrays.sort(reserve);

        HashMap<Integer, Integer> map = new HashMap<Integer,Integer>();
        HashMap<Integer, Integer> Rmap = new HashMap<Integer,Integer>();
        

        for(int lostNum: lost){
            map.put(lostNum,lostNum);
        }
        for (int reserveNum : reserve) {
            Rmap.put(reserveNum, reserveNum);
        }
        for (int reserveNum : reserve) {
            if(map.containsKey(reserveNum)){
                answer++;
                map.remove(reserveNum);
                continue;
            }
            if(map.containsKey(reserveNum-1)){
                System.out.println("-1      "+reserveNum);
                map.remove(reserveNum-1);
                answer++;
            }
            else if(map.containsKey(reserveNum+1)&&!Rmap.containsKey(reserveNum+1)){
                System.out.println("+1       "+reserveNum);
                map.remove(reserveNum+1);
                answer++;
            }
        }
        System.out.println(answer);
        return n-(lost.length-answer);
    }
}