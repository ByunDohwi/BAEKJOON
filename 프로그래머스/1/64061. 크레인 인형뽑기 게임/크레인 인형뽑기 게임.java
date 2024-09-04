/*
1. moves 값이 들어가면 그 자리에 있는 인형을 반환하는 함수를 사용해 인형을 얻는다. 
2. 인형을 스택에 넣는다. 
3. 스택 가장 위에 있는 

[0,0,0,0,0],
[0,0,1,0,3],
[0,2,5,0,1],
[4,2,4,4,2],
[3,5,1,3,1]


**/
import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        Stack<Integer> stack = new Stack<Integer>();
        Integer answer = 0;
        for (int moveTo : moves) {
           boolean isCheckPop = false;
            int num = getDoll(board, moveTo-1);
             if(!stack.isEmpty()){
                if (num == stack.peek()) {
                    stack.pop();
                    answer += 2;
                    isCheckPop = true;
                }
             }
    
                if(num != -1 && !isCheckPop){
                stack.add(num);
                }
            }
        return answer;
    }
    public int getDoll(int[][] board, int moveTo){
        for (int i = 0; i < board[0].length; i++) {
            if (board[i][moveTo] > 0) {
                int doll = board[i][moveTo];
                board[i][moveTo] = 0;
                return doll;
            }
        }
        return -1;
    }
}