#include <iostream>

int main() {
    int a[] = {3, 6, 4, 1, 12, 5, 2, 10, 18};
    std::cout << "Insertion Sort Algorithm" << std::endl;

    std::cout << "UNSORTED ALGORITHM: " << std::endl;
    for (int i = 0; i < 9; i++) {
        std::cout << "a["<< i << "]: " << a[i] << std::endl;
    }

    for (int i = 1; i < 9; i++) {
        int smallest = i;
        while (smallest > 0 && a[smallest] < a[smallest - 1]) {
            int temp = a[smallest];
            a[smallest] = a[smallest - 1];
            a[smallest - 1] = temp;
            smallest--;
        }
    }

    std::cout << std::endl;

    std::cout << "SORTED ARRAY:" << std::endl;
    for (int i = 0; i < 9; i++) {
        std::cout << "a["<< i << "]: " << a[i] << std::endl;
    }
    
    return 0;
}