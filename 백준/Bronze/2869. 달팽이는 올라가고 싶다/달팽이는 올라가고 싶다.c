#include <stdio.h>

int main()
{
    int A, B, V;
    int cnt = 0;
    scanf("%d %d %d", &A, &B, &V);

   cnt = (V-A)/(A-B);
    if((V-A)%(A-B) != 0)
       cnt++;
   printf("%d",cnt+1);
}