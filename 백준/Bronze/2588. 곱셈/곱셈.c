#include <stdio.h>
int main()
{
	int tnum = 0, bnum = 0;
	scanf("%d", &tnum);
	scanf("%d", &bnum);
	for (int i = bnum; i  > 0; i /= 10)
	{
		printf("%d\n", (i%10)*tnum);
	}
	printf("%d", tnum * bnum);

}