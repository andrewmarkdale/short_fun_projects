/*
Andrew Mark Dale
Collatz Conjecture using recursion
*/

#include <stdio.h>
#include <time.h>

int collatz(long long num, int steps){
    if(num == 1){
        return steps;
    }
    else if(num % 2 == 0){
        steps++;
        collatz(num / 2, steps);
    }
    else{
        steps++;
        collatz(3*num + 1, steps);
    }
}

int main(){
    long long inputNum;
    printf("Enter a number: ");
    scanf("%lld", &inputNum);

    clock_t tic = clock();
    printf("The number of steps for %lld is %d\n", inputNum, collatz(inputNum, 0));
    clock_t toc = clock();
    printf("Elapsed: %f seconds\n", (double)(toc - tic) / CLOCKS_PER_SEC);
    return 0;
}