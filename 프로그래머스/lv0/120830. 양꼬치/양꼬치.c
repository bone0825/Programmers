#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n, int k) {
    int j  = n/10;
    printf("%d",j);
    int answer  = (n*12000) + ((k - j)*2000);
    
    return answer;
}