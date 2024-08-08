#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

bool makeString(char str[]) {
    int i = 0, checkture = 0;
    while(*(str+i) != '\0') {
        if(*(str+i) == '(') {
            checkture++;
        }else {
            checkture--;
            if(checkture<0) {
                return false;
            }
        }
        i++;
    }
    if(!checkture) {
        return true;
    }if(checkture) {
        return false;
    }

}
int main(void) {
    int num;
    char str[50];
    scanf("%d", &num);
    for(int i = 0; i<num; i++) {
        scanf("%s",str);
        if(makeString(str)) {
            printf("YES\n");
        }else {
            printf("NO\n");

        }

    }

}
