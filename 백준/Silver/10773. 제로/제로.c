#include <stdio.h>
int main() {
	int n =0, num =0, index_cnt = 0, cnt=0;
    long long int answer=0;
	int arr[100000];
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
        scanf("%d",&num);
        // printf("%d\n",num);
		if (num == 0)
		{
			index_cnt--;
			arr[index_cnt] = 0;
		}
		else if(num != 0){
        arr[index_cnt] = num;
		index_cnt++;
        }
	}
    // printf("index_cnt의 값: %d\n",index_cnt);
    // for(int i = 0;i<index_cnt; i++)
    //     printf("arr[i]의 값: %d\n",arr[i]);
	for (int i = 0; i <index_cnt; i++) {
		answer += arr[i];
	}
	printf("%lld", answer);

}