#include <stdio.h>

int main(void) {
	int tmp;
	int a;
	int min = 1000000000;
	int max = -1000000000;
	scanf("%d", &a);
	for (int i = 0; i < a; i++) {
		scanf("%d", &tmp);
		if (tmp > max) {
			max = tmp;
		}
		if (tmp < min) {
			min = tmp;
		}
	}
	printf("%d %d", min, max);
	return 0;
}