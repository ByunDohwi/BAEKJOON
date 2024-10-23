/*
1. 모든 형을 map으로 등록
2. replace를 사용해 키를 얻고 그에따라 점수 추가하기
3. 각 지표마다 더 높은 유형 추가하기
*/

import java.util.HashMap;

class Solution {
    public String solution(String[] survey, int[] choices) {
        StringBuilder answer = new StringBuilder();
        HashMap<String, Integer> map = new HashMap<>();
        String[] UH = {"R","T","C","F","J","M","A","N"};
        for(String uh : UH){
            map.put(uh, 0);
        }

        for(int i =0; i<survey.length; i++){
            String[] temp = survey[i].split("");
            map.put(temp[choices[i]>3?1:0], map.get(temp[choices[i]>3?1:0])+Math.abs(choices[i]-4)); 
        }
        for(int i = 0; i < UH.length; i+=2){
            if(map.get(UH[i]) < map.get(UH[i+1])){
                answer.append(UH[i + 1]);
            }else{
                answer.append(UH[i]);
            }
        }
        return answer.toString();
    }
}