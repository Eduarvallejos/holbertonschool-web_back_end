# ES6 Basics

¡Bienvenido a mi directorio de ES6 Basics! Aquí encontrarás información y ejemplos básicos sobre las características y funcionalidades introducidas en ECMAScript 6 (también conocido como ES6), la sexta edición del estándar de JavaScript.

## Contenido

1. [Introducción a ES6](#introducción-a-es6)
2. [Variables: let y const](#variables-let-y-const)
3. [Arrow Functions](#arrow-functions)
4. [Parameter defaults](#Parameter defaults)
5. [Template Literals](#template-literals)
6. [Destructuring](#destructuring)
7. [Rest Parameters y Spread Operator](#rest-parameters-y-spread-operator)
8. [Promesas](#promesas)

## Introducción a ES6

ES6, lanzado en 2015, introdujo varias características nuevas y emocionantes a JavaScript que han simplificado el desarrollo y mejorado la legibilidad del código. Este directorio está diseñado para proporcionar una introducción clara y concisa a algunas de las características básicas de ES6.

## Variables: let y const

El uso de `let` y `const` para declarar variables reemplaza en gran medida al uso de `var` en ES5. Aprenderemos sobre las diferencias entre `let`, `const` y `var`, y cuándo es apropiado usar cada uno.

```javascript
// Ejemplo de uso de let
let x = 10;
x = 20; // Se puede reasignar
console.log(x); // Imprime 20

// Ejemplo de uso de const
const y = 30;
// y = 40; // Esto daría un error, no se puede reasignar una constante
console.log(y); // Imprime 30
```

## Parameter defaults

ES6 permite asignar valores por defecto a los parámetros (`Parameter defaults`) de una función, lo que significa que si un argumento no se pasa a la función, se utilizará el valor por defecto especificado.

```javascript
function saludar(nombre = 'Usuario') {
    console.log(`¡Hola, ${nombre}!`);
}

saludar(); // Salida: ¡Hola, Usuario!
saludar('Pedro'); // Salida: ¡Hola, Pedro!
```

## Arrow Functionst

Las funciones de flecha (`arrow functions`) proporcionan una sintaxis más concisa y clara para definir funciones en JavaScript. Exploraremos cómo funcionan y cómo pueden simplificar nuestro código.

```javascript
// Ejemplo de función de flecha
const sumar = (a, b) => a + b;
console.log(sumar(2, 3)); // Imprime 5
```

## Template Literals

Las plantillas de cadena (`template literals`) nos permiten crear cadenas de texto de forma más legible e interpolando variables dentro de ellas. Veremos cómo utilizar esta característica para mejorar la legibilidad de nuestro código.

```javascript
// Ejemplo de uso de template literals
const nombre = 'Juan';
const edad = 30;
console.log(`Hola, me llamo ${nombre} y tengo ${edad} años.`); // Imprime Hola, me llamo Juan y tengo 30 años.
```

## Destructuring

La desestructuración ('destructuring') nos permite extraer valores de arrays y objetos de manera más concisa y expresiva. Aprenderemos cómo usar la desestructuración para trabajar con datos de forma más eficiente.

```javascript
// Ejemplo de desestructuración de arrays
const numeros = [1, 2, 3];
const [num1, num2, num3] = numeros;
console.log(num1, num2, num3); // Imprime 1 2 3
```

## Rest Parameters

Los parámetros rest (`rest parameters`), representado por tres puntos consecutivos(`...`) ,permite a una funcion aceptar un numero variable de argumentos como un array.

```javascript
// Ejemplo de uso de rest parameters
const sumar = (...numeros) => {
  return numeros.reduce((total, num) => total + num, 0);
}
console.log(sumar(1, 2, 3, 4, 5)); // Imprime 15
```
En este ejemplo , la funcion `sumar` puede aceptar cualquier cantidad de argumentos y los trata como un array llamado `numeros`.

## Spread Operator

El operador de propagación (`spread operator`), tambien representado por tres puntos consecutivos(`...`), se utiliza para expandir un array en mutiples elementos.

```javascript
// Ejemplo de uso de spread operator
const numeros1 = [1, 2, 3];
const numeros2 = [4, 5, 6];
const numerosConcatenados = [...numeros1, ...numeros2];
console.log(numerosCombinados); // Imprime [1, 2, 3, 4, 5, 6]
```
En este ejemplo, el operador spread se usa para concatenar los arrays `numeros1` y `numeros2` en uno solo, `numerosConcatenados`.

## Promesas

Las promesas (`promises`) son una forma de manejar operaciones asincrónicas de manera más ordenada y legible. Exploraremos cómo trabajar con promesas para manejar tareas asíncronas de manera efectiva.

```javascript
// Ejemplo de uso de promesas
const miPromesa = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('¡La promesa se ha cumplido!');
  }, 2000);
});

miPromesa.then((mensaje) => {
  console.log(mensaje); // Imprime ¡La promesa se ha cumplido!
});
```

Este README.md proporciona ejemplos prácticos de cada concepto básico de ES6 junto con su descripción, todo en formato de código para resaltar mejor los fragmentos de código. Si necesitas más detalles o tienes alguna pregunta, no dudes en consultar la documentación oficial de JavaScript.