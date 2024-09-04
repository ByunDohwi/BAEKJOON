/*
1. (는 1을 더한고 )는 1을 뺀다. 
**/
public class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int num = 0;
        for(char a : s.toCharArray()){
            if(a == '(')
                num++;
            else
                num--;
            if(num<0) {
                return false;
            }
        }
        return num == 0;
    }
}