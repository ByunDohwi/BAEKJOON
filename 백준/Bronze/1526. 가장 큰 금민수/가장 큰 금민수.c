#include<stdio.h>
int main() {
	int num;
	scanf("%d", &num);
	for (int i = num; i > 0; i--) {
        int t = 1;
		for (int j = i; j > 0; j/=10) {
			int l = j % 10;
			if(l == 4 || l == 7){
                t = 1;
            }
			else {
				t = 0;
				break;
				
			}
		
		}
		if (t == 1) {
			printf("%d",i);
            break;
		}
	}
}