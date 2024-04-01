#include <stdio.h>
int main()
{
	long long int max[3] = { 0 };
	long long int num[7] = { 0 };
	long long int num_s = 0, n = 0,temp=0, answer=0;
	scanf("%lld", &n);
	num_s = n - 2;
	for (int i = 1; i <= 6; i++)
	{
		scanf("%lld", &num[i]);
	}
	max[0] = num[1] < num[6] ? num[1] : num[6];
	max[1] = num[2] < num[5] ? num[2] : num[5];
	max[2] = num[3] < num[4] ? num[3] : num[4];

	for (int i = 2; i > 0; i--) {
		for (int j = 0; j < i; j++) {
			if (max[j] > max[j + 1]) {
				temp = max[j];
				max[j] = max[j + 1];
				max[j + 1] = temp;
			}
		}
	}
	answer += 4*(max[0] + max[1] + max[2]);
	answer += ((num_s * 8) + 4) * (max[0] + max[1]);
	answer += ((5*(num_s*num_s))+(num_s*4)) * max[0];
    if(n == 1)
    {
        for (int i = 6; i > 0; i--) {
		for (int j = 1; j < i; j++) {
			if (num[j] > num[j + 1]) {
				temp = num[j];
				num[j] = num[j + 1];
				num[j + 1] = temp;
			}
		}
        answer = num[1]+num[2]+num[3]+num[4]+num[5];
	}
    }
    
	printf("%lld",answer);
}