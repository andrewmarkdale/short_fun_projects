/*
Andrew Mark Dale
Collatz conjecture
*/

#include <stdio.h>
#include <time.h>

int main(){
    long long inputNum, start, highestNum;
    int steps = 0;

    printf("Enter a number to check: ");
    scanf("%lld", &inputNum);


    clock_t tic = clock();
    start = inputNum;
    highestNum = 0;
    while(start != 1){
        if(start > highestNum) highestNum = start;
        if(start % 2 == 0){
            start = start / 2;
            steps++;
        }
        else{
            start = 3 * start + 1;
            steps++;
        }
    }
    clock_t toc = clock();

    printf("The number of steps for %lld is %d\n", inputNum, steps);
    printf("Highest number achieved: %lld\n", highestNum);
    printf("Elapsed: %f seconds\n", (double)(toc - tic) / CLOCKS_PER_SEC);
    return 0;
}