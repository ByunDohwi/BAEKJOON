#include <stdio.h>
int main() {
	int n =0;
	int arr[500000];
	scanf("%d", &n);
    int front= 1, rear = n, runNum=1;
	for (int i = 1; i < n; i++)
	{
		arr[i] = i;
	}
	arr[0] = n;
	while ((front % n) != (rear%n))
	{
		if (runNum % 2 == 1)
		{
			front++;
			runNum++;
		}
		if(runNum%2 == 0)
		{
			arr[(++rear) % n] = arr[(front++)%n];
			runNum++;
		}
	}
	printf("%d", arr[(front % n)]);
}