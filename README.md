# bubba-lang

## Breve descripción del lenguaje

Hola

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
