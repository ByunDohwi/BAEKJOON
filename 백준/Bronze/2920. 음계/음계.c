#include <stdio.h>
int main()
{
	int a[8] = { 0 };
	int temp = 0;
	for (int i = 0; i < 8; i++)
	{
		scanf("%d", &a[i]);
	}
	for (int i = 0; i < 7; i++)
	{
		if (a[i] - a[i + 1] == 1)
			temp = 1;
		else if (a[i] - a[i + 1] == -1)
			temp = -1;
		else
		{
			temp = 0;
			break;
		}
	}
	if (temp == 1)
		printf("descending");
	else if (temp == -1)
		printf("ascending");
	else
		printf("mixed");
}