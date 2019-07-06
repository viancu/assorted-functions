#include <stdio.h>
#include <stdint.h>

int count_zero_neg(int *arr, size_t n)
{
    int sum = 0, i;

    for (i = n; i > 0; i--)
    {
        sum += !arr[i - 1];
    }
    return ~sum + 1;
}

int main()
{
    int arr[8] = {1, 0, 5, 0, 0, 8, 0, 0};
    printf("This is the number of zeroes... negative: %d\n", count_zero_neg(arr, 8));
    return 0;
}