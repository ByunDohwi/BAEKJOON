#include <stdio.h>
#include <string.h>
int main()
{
	int stack[10000] = { 0 };
	int n, a,num=0;
	char command[10];
	scanf("%d", &n);
	for (int i = 0; i < n; i++ )
	{
		scanf("%s", &*command);
		if (strcmp(command,"push") == 0)
		{
			scanf("%d",&stack[num]);
			num++;
		}
		else if (strcmp(command, "pop") == 0)
		{
            if(num == 0)
                printf("%d\n",-1);
			else{
            printf("%d\n", stack[0]);
			for (int i = 0; i < num; i++)
				stack[i] = stack[i + 1];
			num--;}
		}
		else if (strcmp(command, "size")==0)
		{
			printf("%d\n",num);
		}
		else if (strcmp(command, "empty")==0)
		{
			if (num == 0)
				printf("%d\n", 1);
			else
				printf("%d\n", 0);
		}
		else if (strcmp(command,"front")==0)
		{
			if (num == 0)
				printf("%d\n", -1);
			else
				printf("%d\n", stack[0]);
		}
		else if (strcmp(command, "back")==0)
		{
			if (num == 0)
				printf("%d\n", -1);
			else
				printf("%d\n", stack[num-1]);
		}

	}

}