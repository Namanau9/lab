#include <stdio.h>
#include <stdlib.h>

int count;

void merge(int a[10], int left, int mid, int right) {
    int i, j, k, b[10];
    i = left;
    j = mid + 1;
    k = left;

    while ((i <= mid) && (j <= right)) {
        count++;
        if (a[i] < a[j]) {
            b[k++] = a[i++];
        } else {
            b[k++] = a[j++];
        }
    }

    while (i <= mid)
        b[k++] = a[i++];

    while (j <= right)
        b[k++] = a[j++];

    for (i = left; i <= right; i++)
        a[i] = b[i];
}

void mergesort(int a[10], int left, int right) {
    int mid;
    if (lef
