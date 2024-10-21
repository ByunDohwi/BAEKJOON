class Solution {
    public static int a(int n){
        int sum =0;
        for(int i = 1; i <= n; i++){
            sum += i;
        }
        return sum;
    }
    
    public static int[] solution(int n) {

        int[] answer = new int[a(n)];
        int nowPoint = 0;
        int count = 0;
        int a= n;
        int b = 0;
        for (int i = 1; i <= n; i++) {
            if (i % 3 == 1) {
                int y = b;
                for (int j = 0; j <= n-i; j++) {
                    nowPoint += y++;
                    answer[nowPoint] = ++count;
                }
                b += 2;
            } else if (i % 3 == 2) {
                for (int j = 0; j <= n-i; j++) {
                    answer[++nowPoint] = ++count;
                }
            } else if (i % 3 == 0) {
                int x = a;
                for (int j = n-i; j >= 0; j--) {
                    nowPoint -= x--;
                    answer[nowPoint] = ++count;
                }
                a--;

            }
        }

        return answer;
    }
}