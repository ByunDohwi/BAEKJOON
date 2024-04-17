#include <stdio.h>
int main()
{
	int a =1, b;
	char name [11];
	while (1)
	{
		scanf("%s %d %d", name, &a, &b);
		if (a == 0)
			break;
		if (a > 17 || b >= 80)
			printf("%s Senior\n", name);
		else
			printf("%s Junior\n", name);

	}
	
}