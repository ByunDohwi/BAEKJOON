import java.util.Arrays;
/*

1. 배열을 정렬하기
2. 시작과 끝을 더해보기
2-1. limit보다 작으면 둘이 같이 태우기
2-2. ㅣimit보다 크면 혼자태우고 end를 줄이기

*/
import java.util.Arrays;

class Solution {
    public int solution(int[] people, int limit) {
        Arrays.sort(people);
        int start =0, end = people.length-1;
        int answer = 0;

        while(start<=end){
            if(people[start]+people[end] <= limit){
                answer++;
                start++;
                end--;
            }else{
                answer++;
                end--;
            }
        }

        return answer;
    }
}