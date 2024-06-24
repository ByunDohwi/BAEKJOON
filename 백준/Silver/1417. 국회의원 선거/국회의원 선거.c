#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>
#include<string.h>
int main() {
	int n;
	int max[1][2] = { -1,-1 };//1인덱스 2값
	int cnt = 0;

	scanf("%d", &n);

	int* p = (int*)malloc(sizeof(int) * n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &p[i]);
        if (max[0][1] < p[i] && i != 0) {
				max[0][0] = i;
				max[0][1] = p[i];
			}
	}

	while (1) {
		for (int i = 0; i < n; i++)
		{
			if (max[0][1] <= p[i] && i != 0) {
				max[0][0] = i;
				max[0][1] = p[i];
			}
		}
		if (p[0] > max[0][1]) {
			break;
		}
		p[max[0][0]]--;
        max[0][1]--;
		p[0]++;
        cnt++;
        
	}
	printf("%d", cnt);
}