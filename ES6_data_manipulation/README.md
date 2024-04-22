# Manipulación de datos en ES6

La manipulación de datos en ECMAScript 6 (ES6) ha sido mejorada con la introducción de una serie de características nuevas y útiles. Estas características hacen que trabajar con datos en JavaScript sea más eficiente y legible. En este documento, exploraremos algunas de estas características y cómo se pueden utilizar para manipular datos de manera efectiva.

---
## Contenido

1. [Métodos de Arrays: `map()`, `filter()` y `reduce()`](#Métodos-de-Arrays:-`map()`-,-`filter()`-y-`reduce()`)
2. [Typed Arrays](#Typed-Arrays)
3. [Estructuras de datos: `set`, `Map` y `WeakMap`](#Estructuras-de-datos:-`set`,-`Map`-y-`WeakMap`)

---

## Métodos de Arrays: `map()`, `filter()` y `reduce()`

Los métodos `map()`, `filter()` y `reduce()` son fundamentales para manipular arrays en JavaScript.

- **`map()`:** Se utiliza para transformar cada elemento de un array aplicando una función a cada uno de ellos y devolviendo un nuevo array con los resultados.

```javascript
const numbers = [1, 2, 3, 4, 5];

// Duplicar cada número en el array usando map()
const doubledNumbers = numbers.map(num => num * 2);

console.log(doubledNumbers); // Output: [2, 4, 6, 8, 10]

```

- **`filter()`:** Se utiliza para crear un nuevo array con todos los elementos que cumplan ciertos criterios especificados en una función.

```javascript
const numbers = [1, 2, 3, 4, 5];

// Filtrar solo los números pares usando filter()
const evenNumbers = numbers.filter(num => num % 2 === 0);

console.log(evenNumbers); // Output: [2, 4]

```

- **`reduce()`:** Se utiliza para reducir los elementos de un array a un solo valor aplicando una función a cada elemento del array.

```javascript
const numbers = [1, 2, 3, 4, 5];

// Sumar todos los números en el array usando reduce()
const sum = numbers.reduce((accumulator, currentValue) => accumulator + currentValue, 0);

console.log(sum); // Output: 15

```
## Typed Arrays

Los Typed Arrays son estructuras de datos en JavaScript que proporcionan una forma de acceder y manipular datos binarios de manera más eficiente que los arrays normales. Están diseñados para trabajar con datos numéricos y de bytes de manera más eficiente y segura en términos de memoria y rendimiento.


Hay varios tipos de Typed Arrays disponibles en JavaScript, cada uno diseñado para trabajar con un tipo específico de datos:

1. **`Int8Array, Uint8Array, Uint8ClampedArray`:** Estos tipos de arrays están diseñados para trabajar con datos de 8 bits sin signo (Uint8Array), datos de 8 bits con signo (Int8Array) y datos de 8 bits clamped (Uint8ClampedArray), que son utilizados comúnmente en el contexto de imágenes y gráficos.
2. **`Int16Array, Uint16Array`:** Estos tipos de arrays trabajan con datos de 16 bits, ya sea con o sin signo.
3. **`Int32Array, Uint32Array`:** Similar a los anteriores, pero para datos de 32 bits.
4. **`Float32Array, Float64Array`:** Estos tipos de arrays están diseñados para trabajar con datos de punto flotante de precisión simple (32 bits) y doble precisión (64 bits), respectivamente.

```javascript
// Crear un nuevo array tipado de enteros de 8 bits con longitud 3
const int8Array = new Int8Array(3);

// Asignar valores al array
int8Array[0] = 10;
int8Array[1] = 20;
int8Array[2] = 30;

console.log(int8Array); // Output: Int8Array [10, 20, 30]

```
## Estructuras de datos: `set`, `Map` y `WeakMap`

- **`set`:**: El objeto Set en JavaScript es una colección de valores únicos, lo que significa que no puede contener duplicados.

```javascript
// Crear un nuevo conjunto
const mySet = new Set();

// Añadir elementos al conjunto
mySet.add(1);
mySet.add(2);
mySet.add(3);
mySet.add(1); // Este valor se ignora porque ya existe en el conjunto

console.log(mySet); // Output: Set {1, 2, 3}

```

- **`Map`:** El objeto Map en JavaScript es una colección de pares clave-valor donde las claves pueden ser de cualquier tipo de datos.

```javascript
// Crear un nuevo mapa
const myMap = new Map();

// Añadir elementos al mapa
myMap.set('key1', 'value1');
myMap.set('key2', 'value2');

console.log(myMap.get('key1')); // Output: value1

```

- **`WeakMap`:** WeakMap es similar a Map, pero solo acepta objetos como claves y mantiene las referencias débiles a los objetos almacenados en él.

```javascript
// Creamos un WeakMap
let weakMap = new WeakMap();

// Creamos un objeto como clave
let objetoClave = {};

// Asociamos un valor con la clave en el WeakMap
weakMap.set(objetoClave, "Valor asociado");

// Verificamos si el objeto clave existe en el WeakMap
console.log(weakMap.has(objetoClave)); // Salida: true

// Eliminamos la referencia al objeto clave
objetoClave = null;

// En este punto, el objeto clave podría ser recolectado por el recolector de basura
// Si intentamos verificar si el objeto clave existe en el WeakMap, obtendremos false
console.log(weakMap.has(objetoClave)); // Salida: false

```
Estas características de ES6 proporcionan herramientas poderosas para manipular datos de manera efectiva en JavaScript. Al utilizar métodos de arrays, arrays tipados y estructuras de datos como Set, Map y WeakMap, puedes escribir código más limpio, eficiente y legible para manipular datos en tus aplicaciones JavaScript.