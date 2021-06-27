#include <iostream>

using namespace std;

int main() {
    int a, b;
    while (scanf("%d %d", &a, &b) == 2) {
        int sum = a * 2 * b;
        printf("%d", sum);
    }
    return 0;
}