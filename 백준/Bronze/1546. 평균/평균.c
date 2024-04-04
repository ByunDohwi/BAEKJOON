#include <stdio.h>
int main() {
	int n = 0, max = -1;
	double num = 0, answer =0;
	double arr[10000];
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%lf", &arr[i]);
			if(arr[i] > max)
				max = arr[i];
	}
	for (int i = 0; i < n; i++)
	{
		answer += arr[i] / max * 100;
	}
	printf("%f", answer / n);
}