prog  Fibonacci:

vars {
    int : iterative, recursion, n;
}


func int fibonacciIterative(int : n) {
    vars {
        int : i, prev, prevprev, curr;
    }
    prevprev = 0;
    prev = 0;
    curr = 1;
    i = 1;

    while (i < n) {
        prevprev = prev;
        prev = curr;
        curr = prevprev + prev;
        i = i + 1;
    }
    return curr;
}

func int fibonacciRecursive(int : n) {
    if (n <= 0) {
        return 0;
    };
    
    if (n == 1) {
        return 1;
    };

    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}


main() {
    input(n);
    iterative = fibonacciIterative(n);
    recursion = fibonacciRecursive(n);
    print(iterative);
    print("\n");
    print(recursion);

}

