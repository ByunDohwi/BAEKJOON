#include <stdio.h>
int answer =0;
int sosu(int x)
{
    if(x == 1)
        return 0;
    for(int i = x-1; i >= 2; i--)
        {
            if(x%i == 0)
                return answer;
        }
    return ++answer;
}
int main() {
	int n =0, num =0, index_cnt = 0, cnt=0;
    scanf("%d",&n);
   for(int i = 0; i < n; i++)
        {
        scanf("%d",&num);
        sosu(num);
        }
    printf("%d",answer);

}