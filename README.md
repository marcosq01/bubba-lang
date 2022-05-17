# bubba-lang

## Breve descripción del lenguaje

Lenguaje de tipado estático orientado a objetos.

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
