#include <stdio.h>
int main()
{
	int a, b, i, j, k, l, m = 0, n = 0, answer = 0, w_max = 99999999, b_max = 9999999,b_answer=0;
	char borad_color[51][51];
	int white_arr[50][50] = { 0 }, black_arr[50][50] = { 0 };
	scanf("%d %d", &a, &b);//a는 입력받은 보드의 세로, b는 가로
	for (int i = 0; i < a; i++)
	{
		scanf("%s", &borad_color[i][0]);//borad_color에 bw가 저장됨
	}

	for (i = 0; i < a; i++)//첫 번째 블럭이 하얀색일때, 바꿔야하는 인덱스 번호를 1로 저장ㅊ
	{
		if (i % 2 == 1)// i = 0, b =8, a =8
			j = 1;
		for (j; j < b; j += 2)
		{
			if (borad_color[i][j] == 'B')
				white_arr[i][j]++;
		}
		if (i % 2 == 0)
			k = 1;
		for (k; k < b; k += 2)
		{
			if (borad_color[i][k] == 'W')
				white_arr[i][k]++;
		}
		j = 0, k = 0;

	}
	for (l = 0; l < a; l++)//첫 번째 블럭이 하얀색일때, 바꿔야하는 인덱스 번호를 1로 저장ㅊ
	{
		if (l % 2 == 1)// i = 0, b =8, a =8
			m = 1;
		for (m; m < b; m += 2)
		{
			if (borad_color[l][m] == 'W')
				black_arr[l][m]++;
		}
		if (l % 2 == 0)
			n = 1;
		for (n; n < b; n += 2)
		{
			if (borad_color[l][n] == 'B')
				black_arr[l][n]++;
		}
		m = 0, n = 0;

	}
	for (int i = 0; i < a - 7; i++) {
		for (int j = 0; j < b - 7; j++) {

			for (int k = i; k < i + 8; k++)
			{
				answer += (white_arr[k][j] + white_arr[k][j + 1] + white_arr[k][j + 2] + white_arr[k][j + 3] + white_arr[k][j + 4] + white_arr[k][j + 5] + white_arr[k][j + 6] + white_arr[k][j + 7]);
			}

			if (w_max > answer)
				w_max = answer;
			answer = 0;
		}
	}
	for (int i = 0; i < a - 7; i++) {
		for (int j = 0; j < b - 7; j++) {

			for (int k = i; k < i + 8; k++)
			{
				b_answer += (black_arr[k][j] + black_arr[k][j + 1] + black_arr[k][j + 2] + black_arr[k][j + 3] + black_arr[k][j + 4] + black_arr[k][j + 5] + black_arr[k][j + 6] + black_arr[k][j + 7]);
			}

			if (b_max > b_answer)
				b_max = b_answer;
			b_answer = 0;
		}
	}


	printf("%d\n", (w_max>b_max?b_max:w_max));
	

	// for (int i = 0; i < a; i++)
	// {
	// 	for (int j = 0; j < b; j++)
	// 	{
	// 		printf("%d", white_arr[i][j]);
	// 	}
	// 	printf("\n");
	// }


}