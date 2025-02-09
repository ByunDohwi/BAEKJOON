int main(void)
{
	int N;
	scanf("%d", &N);
	int arr[5001] = { 0};
	arr[3] = 1;
	arr[5] = 1;
	for (int i = 6; i <= 5000; i++) {
		if (arr[i - 3]) {
			arr[i] = arr[i - 3] + 1;
		}
		if (arr[i - 5]) {
			if (arr[i])
				arr[i] = arr[i - 5] + 1 < arr[i] ? arr[i - 5] + 1 : arr[i];
			else	
				arr[i] = arr[i - 5] + 1;
		}
	}
	if (arr[N])
		printf("%d", arr[N]);
	else
		printf("-1");
}