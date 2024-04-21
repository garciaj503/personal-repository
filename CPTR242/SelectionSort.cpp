#include <iostream>

int main() {
    int a[] = {3, 6, 4, 1, 12, 5, 2, 10, 18};
    std::cout << "Selection Sort Algorithm" << std::endl;

    std::cout << "UNSORTED ALGORITHM: " << std::endl;

    for (int i = 0; i < 9; i++) {
        std::cout << "a["<< i << "]: " << a[i] << std::endl;
    }

    for (int i = 0; i < 8; i++) {
        int min = i;
        for (int j = i + 1; j < 9; j++) {
            if (a[j] < a[min]) {
                min = j;
            }
        }
        int temp = a[i];
        a[i] = a[min];
        a[min] = temp;
    }

    std::cout << std::endl;

    std::cout << "SORTED ARRAY:" << std::endl;
    for (int i = 0; i < 9; i++) {
        std::cout << "a["<< i << "]: " << a[i] << std::endl;
    }
    
    return 0;
}