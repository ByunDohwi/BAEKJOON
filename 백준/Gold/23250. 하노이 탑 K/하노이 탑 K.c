#include <stdbool.h>
#include <stdio.h>
long long int k;
void hanoi( long long int hanoiNum,long long int nextNum, int from, int work, int to) {
	if(hanoiNum > k) {
		hanoi(hanoiNum-nextNum,nextNum>>1,from,to,work);
	}else if(hanoiNum == k) {
		printf("%d %d",from,to);
	}else {
		hanoi(hanoiNum+nextNum,nextNum>>1,work,from,to);
	}

}
int main() {
    int n;
	scanf("%d %lld",&n,&k);
	long long int hanoiNum = (long long int)1<<n-1;
	long long int nextNum = (long long int)1<<n-2;
	hanoi(hanoiNum,nextNum,1,2,3);
}