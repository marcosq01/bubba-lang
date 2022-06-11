prog matrices:

vars {
    int : A[4, 3], B[3, 4], C[4, 4];
}


func void llenarMatrices() {
    vars {
        int : i, j;
    }
    for i in 0..3 step 1 {
        for j in 0..2 step 1 {
            A[i, j] = j;
        }
    }

    for i in 0..2 step 1 {
        for j in 0..3 step 1 {
            B[i, j] = j;
        }
    }
}

func void multiplicarMatrices() {
    vars {
        int : i, j, k;
    }

   for i in 0..3 step 1 {
       for j in 0..3 step 1 {
           for k in 0..2 step 1 {
               C[i, j] = C[i, j] + A[i, k] * B[k, j];
           }
       }
   }

    for i in 0..3 step 1 {
       for j in 0..3 step 1 {
           print(C[i, j]);
           print(" ");
       }
       print("\n");
   }


}

main () {
    llenarMatrices();
    multiplicarMatrices();

}

