class Solution {
    public int[] solution(String[] wallpaper) {
        int[] answer = new int[4];//오른쪽 위, 왼쪽 아래, 세가세가
        int x1 = wallpaper[0].length(), y1 = wallpaper.length, x2 = 0, y2=0;

        for(int i = 0; i < wallpaper.length; i++){//y
            char[] chars = wallpaper[i].toCharArray();
            boolean isUsed = false;
            for(int j = 0;j < chars.length; j++){//x
                if(chars[j] == '#'){
                    isUsed = true;
                    if(x1 > j)
                        x1 = j;
                    if(x2 < j)
                        x2 = j;
                }
            }
            if(isUsed){
                if(y1 > i)
                    y1=i;
                if(y2 < i)
                    y2 = i;
            }
        }
        answer[0] = y1;
        answer[1] = x1;
        answer[2] = y2+1;
        answer[3] = x2+1;

        return answer;
    }
}