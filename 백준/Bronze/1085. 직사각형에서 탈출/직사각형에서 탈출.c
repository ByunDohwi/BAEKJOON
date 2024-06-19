#include<stdio.h>

int main() {

	int x, y, w, h, min = 2100000000;
	scanf("%d %d %d %d", &x, &y, &w, &h);
	if (min > w - x) {
		min = w - x;
	}
	if (min > x) {
		min = x;
	}
	if (min > h - y) {
		min = h - y;
	}
	if (min > y) {
		min = y;
	}
	printf("%d", min);



	
}