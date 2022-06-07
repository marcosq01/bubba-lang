# bubba-lang

## Breve descripción del lenguaje

Lenguaje de tipado estático orientado a objetos.

## Manual de uso

### Requerimientos del sistema

Por el momento ```Bubba``` solo funciona en MacOS y Linux.
Windows no.

Se requiere tener instalado Python 3.

### Compilar y ejecutar

El archivo a compilar y el directorio actual de la terminal deben estar ubicados en la carpeta ```/compiler``` y correr ```bubba.py``` seguido del nombre del archivo con su extensión.

Ejemplo

```
 ~/Desktop/bubba-lang/compiler % python3 bubba.py test.txt
```

### Estructura general

Se debe especificar en la primera línea del código lo siguiente:\
&nbsp;
```
prog NOMBRE_PROGRAMA:

[declaración de clases]

[declaración de variables globales]

[declaración de funciones]


main() {
  [estatutos]
}
```

Las variables globales pueden ir antes de la declaración de clases y viceversa, pero funciones deben ir despues de estas dos.\
De igual forma, no es necesario incluir clases, variables globales o funciones.
  
### Declaración de clases

Para declarar una clase se usa la siguiente sintaxis:

```
class NOMBRE_CLASE {
  attributes {
    TIPO_SIMPLE_1 : ATRIBUTO_1;
    TIPO_SIMPLE_2 : ATRIBUTO_2, ATRIBUTO_3, ...;
  }
};
```

Si se requiere heredar atributos de otra clase se hace lo siguiente:

```
class A extends B {
 ...
};
```

### Declaración de variables (sirve para locales tambien)

La declaración de variables sigue la siguiente estructura:

``` 
vars {
       TIPO_VARIABLE_1 : NOMBRE_1;
       TIPO_VARIABLE_2 : NOMBRE_2, NOMBRE_3, ...;
}
```
Para declarar arreglos o matrices se usa la siguiente sintaxis:

```
vars {
    TIPO : NOMBRE[INT], NOMBRE_2[INT, INT];
}

```
Es necesario que sean INTS los tamanos de los arreglos y matrices, no se permiten expresiones.
Ejemplo:

```
vars {
  float : arr[4], mat[5,5];
}
```
 
 ### Declaración de funciones
 
 La declaración de funciones sigue la siguiente estructura:
 
 ```
 func TIPO_RETORNO NOMBRE_FUNCION (TIPO_PARAMETRO : NOMBRE_PARAMETRO_1, ...) {
    [variables locales]
    [estatutos]
 }
```

Los parámetros son opcionales y los tipos de retorno disponibles para funciones son ```int```, ```float```, ```string``` y ```void```. 

En caso de ser función no ```void``` es obligatorio que haya un ```return expresion``` donde la expresión debe ser del mismo tipo de la función.

Los estatutos de ```return``` pueden estar en cualquier parte de la función.

En funciones ```void``` se puede usar ```return ;``` para terminar la ejecución de la función en cualquier punto.
Dentro de ```main``` no es posible declarar variables. Las variables globales van fuera y antes de ```main```.

---
### Estatutos

#### Asignación

La estructura del estatuto de asignación es la siguiente:

```
VAR = expresion; 
```

Donde ```VAR``` puede ser: ```id```, ```id.id```, ```id[expresion]``` y ```id[expresion, expresion]```.

#### Estatutos condicionales

##### if

La estructura del ```if``` es la siguiente:

```
if (expresión) {
    [estatutos]
};

```

##### if else

La estructura del ```if else``` es la siguiente:

```
if (expresion) {
    [estatutos]
} else {
    [estatutos]
};

```
Es requerido que la expresión dentro de los paréntesis sea de tipo ```int```.

Las expresiones relacionales (```<```, ```>```, ```==```) siempre regresan un valor tipo ```int```.

#### Estatutos cíclicos

##### while

La estructura de ```while``` es la siguiente:

```
while (expresion) {
    [estatutos]
}
```

#### Llamadas a funciones

Puede haber llamadas a funciones como estatutos. No es necesario que la función sea ```void```.

La estructura es la siguiente:

```
funcion();
```

```
funcion(a, b, c);
```

#### Print

La estructura del ```print``` es la siguiente:

```
print(expresion);
```
Sirve para imprimir en pantalla la expresion y dejar un salto de línea.

#### Input

La estructura del ```input``` es la siguiente:

```
input(VAR);
```
Sirve para asignar un valor a ```VAR``` desde la consola. Es necesario que lo ingresado en consola sea del mismo tipo que ```VAR```.

---
### Expresiones

#### Operadores aristméticos 

Los operadores aritméticos disponibles son los siguientes

> ```+```
> ```-```
> ```*```
> ```/```

Siguen las reglas de precendencia normales y se pueden agrupar con paréntesis.

Ejemplo de uso:

```
a = 4 + 4;
b = a * (b + c / 10);
```

#### Operadores relacionales

Los operadores relacionales disponibles son los siguientes

> ```>```
> ```>=```
> ```<```
> ```<=```
> ```==```
> ```!=```

Siguen las reglas de precendencia normales y se pueden agrupar con paréntesis.

Ejemplo de uso:

```
if (a < b) {
...
};

if (x != "a") {
  ...
};
```

#### Operadores booleanos

Los operadores booleanos disponibles son los siguientes (and, or, not, en ese orden):

> ```&&```
> ```||```
> ```!```

El operador not ```!``` es unario. El operador ```&&``` tiene mayor precedencia que ```||```.
Ejemplo de uso:

```
if (a < b && b > 0) {
...
};

if (!(x == 3) || y) {
  ...
};
```

### Llamada a función como un término

Es posible que las funciones regresen valores. Un ejemplo es el siguiente:

```
a = 5 * f();
b = get(x, y);
```

### Elementos de arreglos o matrices

Los arreglos y matrices están indexados a partir del 0.

Se usa la siguiente sintaxis:

```
ARREGLO[expresion]
MATRIZ[expresion, expresion]
```
Ejemplo de uso:

```
a = arr[i + 1];
print(mat[a * x, b + y]);
```

### Atributos de objetos

Para acceder a atributos de un objeto se usa el operador ```.```

Ejemplo:

```
a = obj.nombre;
obj.edad = 18;
```


### Comentarios en el código

Se usa el caracter ```#```  para comentar una línea

Ejemplo:

```
# suma de a y b
x = a + b; 

y = 100;  # esto es un comentario
```

---
### Ejemplo de programa

```
prog bubba:

class A {
    attributes {
        int : a;
        string : s;
    }
};


class B extends A {
    attributes {
        int : b;
    }
};

vars { 
    B : bb;
    A : aa;
}

func int suma(int : a, int : b) {

    if (a > 0) {
        return a + b;
    };
   
    return b;

}


main() {
    bb.a = 10;
    bb.s = "hola desde b";
    aa.a = 50;
    print(bb.a);
    print(aa.a * 1000);
    print(suma(bb.a, aa.a);
}

```

## Avances semanales

### Avance 0

En este avance se hizo el diseño de la estructura general del lenguaje, así como sus funcionalidades, sintaxis, etc.
Se desarrolló un diagrama de sintaxis donde se describen todas las reglas de la gramática de Bubba. También se incluye la lista de los tokens del lenguaje.

Tuvimos unos errores al momento de pasar el bosquejo de la sintaxis a su forma digital, por lo que hubo algunos detalles de las reglas faltantes y nos retrasamos un poco.
Tambien pasamos los diagramas de sintaxis a su forma de gramática.

### Avance 1

Con la gramática y los tokens terminados, procedimos a usar algún generador de Parser para nuestro compilador. 
En nuestro caso usamos ANTLR para el lenguaje Python (el que se usará para el compilador).

Pasar la gramática a ANTLR fue tarea fácil ya que la sintaxis es muy parecida. Se crearon algunos archivos de prueba con lenguaje Bubba, para poner a prueba la gramática.
El archivo test.py imprime los errores(si existen) de cada uno de los archivos prueba.

### Avance 2

En este avance construímos el cubo semántico, para este mismo decidimos utilizar un diccionario para poder acceder facilmente a los valores. Además de ello corregimos algunos errores de acceso a las valores de arreglos dentro de la gramática. Se hizo un diseño de la tabla de directorio de variables pero no tuvimos tiempo de  implementarlo.

### Avance 3

En este avance si creamos la estructura del directorio de variables, la estructura de los cuádruplos e incluso un avance de la estructura del directorio de funciones. Comenzamos a implementar los puntos neurálgicos: para la declaración de variables, checar errores de tipos, generación de cuádruplos para estatutos lineales.


### Avance 4

En este avance implementamos el directorio de funciones, modificamos el manejo de las variables para ahora guardar la dirección y así mismo delimitamos los números de direcciones. Generamos los cuádruplos para los condicionales y el while, creamos e implementamos la tabla de constantes y guardamos los tipos de parámetros de las funciones.

### Avance 5

En este avance se añadió la generación de cuádruplos correspondientes a la declaración y a la llamada de funciones (era, gosub, parameter, endfunc).
También se hizo la contabilización de variables locales y temporales por cada tipo de dato en cada función.
Esta información se utilizará más adelante para el manejo de memoria de la máquina virtual. En las llamadas a funciones se lleva a cabo la verificación de que los argumentos sean los correctos (tipos) con respecto a los parámetros que recibe la función que está siendo llamada.
Para el próximo avance se agregará lo necesario para el return statement de las funciones que no son tipo void.


### Avance 6

En este avance se añadió la generación de cuádruplos para output y la revisión de las funciones no void para que tuvieran un return. Se agregaron reglas para añadir los arreglos a la tabla de variables con los respectivos tamaños de sus dimensiones. En el uso de arreglos como expresiones se verifica que el tamaño de las dimensiones a las que se quiere acceder se encuentren dentro del rango de tamaño del arreglo guardado y que la cantidad de dimensiones sea coherente con la se tiene guardada en la tabla. Además de generar los cuádruplos para la verificación, uno de multiplicación y suma para el caso de la matriz y uno de address que es para generar el pointer. 

### Avance 7

Para este avance se creó el 'esqueleto'  de la maquina virtual y también el mapa de memoria el cual nos sirve para asignar las variables por cada llamada
a funciones. También se corrigieron algunos detalles o errores.
### Avance 8

Para este último avance la máquina virtual ya es capaz de generar código para las expresiones aritméticas, estatutos secuenciales, condicionales y funciones. Además se arreglaron detalles del parser como el manejo de las constantes negativas y el return en void. 


