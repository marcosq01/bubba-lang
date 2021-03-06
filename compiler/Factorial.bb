prog Factorial:

vars {
    int : recursive, iterative, n;
}

func int factorialRecursion(int : n) {
    if (n <= 1) {
        return 1;
    };
    return n * factorialRecursion(n - 1);
}


func int factorialIterative(int : n) {
    vars {
        int : i, res;
    }

    i = 1;
    res = 1;

    while (i <= n) {
        res = res * i;
        i = i + 1;
    }

    return res;
}

main() {
    input(n);
    iterative = factorialIterative(n);
    recursive = factorialRecursion(n);
    print(iterative);
    print("\n");
    print(recursive);
}

