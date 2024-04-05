#include <stdio.h>
int main()
{
	int cnt = 0, m = 1, n = 0;
	long long int i, answer;
	long long int arr[10000] = { 0 };
    	scanf("%d", &n);
	for (i = 666; i < 2100000000; i++)
	{
		for (int j = i; j > 665; j /= 10)
		{
			answer = j % 1000;
			// printf("%lld %d ",answer,j);
			if (answer == 666)
			{
				cnt = 1;
				continue;
			}
		}

		if (cnt == 1)
		{
			arr[m] = i;
			m++;
		}
		if (m - 1 == n)
		{
			break;
		}
		cnt = 0;
		// printf("\n");
	}
	printf("%lld", arr[n]);

}