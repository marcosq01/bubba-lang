prog QuickSort:

vars {
    int : A[10], i, SIZE;
    string : s;
}

func int partition(int : low, int : high) {
    vars {
        int : pivot, i, j, temp;
    }

    pivot = A[high];
    i = low - 1;
    j = low;
    while (j < high) {
        if (A[j] <= pivot) {
            i = i + 1;

            temp = A[i];
            A[i] = A[j];
            A[j] = temp;

        };

        j = j + 1;
    }

    temp = A[i + 1];
    A[i + 1] = A[high];
    A[high] = temp;

    return i + 1;

}

func void quicksort(int : low, int : high) {
    vars {
        int : pi;
    }
    if (low < high) {
        pi = partition(low, high);
        quicksort(low, pi - 1);
        quicksort(pi + 1, high);
    };
}

main() {

    SIZE = 10;

    A[0] = 5;
    A[1] = 4;
    A[2] = 7;
    A[3] = 10;
    A[4] = 1;
    A[5] = 3;
    A[6] = 0;
    A[7] = 2;
    A[8] = -7;
    A[9] = 8;

    quicksort(0, SIZE-1);

    i = 0;
    
    while (i < SIZE) {
        print(A[i]);
        print("\n");
        i = i + 1;
    }

}

