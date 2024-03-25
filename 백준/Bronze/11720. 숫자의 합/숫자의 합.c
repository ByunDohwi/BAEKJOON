#include <stdio.h>
int main() {
	int n, answer = 0, num =0;
	char arr[101];
	scanf("%d", &n);
	scanf("%s", arr);
	for (int i = 0; i < n; i++)
	{
		answer += arr[i] - 48;
	}
	printf("%d", answer);
}
