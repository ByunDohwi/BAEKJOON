import java.io.*;
import java.util.*;

class Solution {
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        List<Integer[]> answer = new ArrayList();

        int extNum = makeNum(ext);
        int sortNum = makeNum(sort_by);
        for (int i = 0; i < data.length; i++) {
            if (data[i][extNum] < val_ext) {
                answer.add(Arrays.stream(data[i]).boxed().toArray(Integer[]::new));
            }
        }

        return answer.stream().map(arr -> Arrays.stream(arr).mapToInt(i->i).toArray()).sorted(Comparator.comparing(a->a[sortNum])).toArray(int[][]::new);
    }
    public int makeNum(String string){//HashMap 사용해보긔
        if (string.equals("code")) {
            return 0;
        }
        if (string.equals("date")) {
            return 1;
        }
        if (string.equals("maximum")) {
            return 2;
        }
        else {
            return 3;
        }
    }
}
