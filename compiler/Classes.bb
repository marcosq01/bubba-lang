prog clases:


class Animal {
    attributes {
        int : edad;
        string : sonido;
    }
};


class Perro extends Animal {
    attributes {
        int : numColmillos;
    }
};

vars {
    Perro : supercan;
}

main() {
    supercan.edad = 100;
    supercan.sonido = "guau";
    supercan.numColmillos = 20 * 2;

    print(supercan.edad);
    print("\n");
    print(supercan.sonido);
    print("\n");
    print(supercan.numColmillos);
    print("\n");

}

