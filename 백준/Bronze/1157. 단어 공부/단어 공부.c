#include <stdio.h>
#include <string.h>
int main()
{
    char arr[1000000];
    int result[30] = { 0 }, answer = 0, temp = 0, max =0, cnt=0, index = 0;
    scanf("%s", arr);
    for (int i = 0; arr[i] != '\0'; i++)
    {
        if (arr[i] >= 97)
            arr[i] -= 32;
        result[arr[i] - 'A']++;
    }
    for (int i = 0; i < 26; i++)
    {
        if (temp < result[i])
        {
            temp = result[i];
            max = result[i];
            index = i;
        }
    }
    for (int i = 0; i < 26; i++)
    {
        if (max == result[i])
            cnt++;
    }
    if (cnt > 1)
        printf("?");
    else
        printf("%c", index + 'A');
}