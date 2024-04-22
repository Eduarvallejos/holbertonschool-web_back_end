
# ES6 Promises

Las promesas en ECMAScript 6 (ES6) son una característica fundamental que proporciona una forma más flexible y legible de trabajar con operaciones asíncronas en JavaScript. En este documento, exploraremos cómo y por qué utilizar promesas, así como los métodos y operadores asociados.

---
## Contenido

1. [Promesas (cómo, por qué y qué)](#Promesas(cómo,-por-qué-y-qué))
2. [Métodos then, resolve y catch](#Métodos-then,-resolve-y-catch)
3. [Uso del método every del objeto Promise](#Uso-del-método-every-del-objeto-Promise)
4. [Throw / Try](#Throw-/-Try)
5. [El operador await](#El-operador-await)
6. [Cómo utilizar una función async](#Cómo-utilizar-una-función-async)

---

## Promesas (cómo, por qué y qué)

Las promesas son objetos que representan la eventual finalización (o falla) de una operación asíncrona y su valor resultante. Se utilizan para manejar operaciones asíncronas de manera más intuitiva y eficiente, evitando el anidamiento excesivo de callbacks y mejorando la legibilidad del código.

```javascript
// Ejemplo de creación de una promesa
const myPromise = new Promise((resolve, reject) => {
  // Ejecutar una operación asíncrona
  setTimeout(() => {
    // Resolve la promesa si la operación es exitosa
    resolve('Éxito');
  }, 1000);
});

```
## Métodos then, resolve y catch

Los métodos `then`, `resolve` y `catch` son fundamentales para trabajar con promesas en JavaScript.

- **`then`:** Se utiliza para especificar qué hacer cuando una promesa se resuelve exitosamente.

```javascript
myPromise.then((result) => {
  console.log(result); // Output: Éxito
});

```
- **`resolve`:** Se utiliza dentro del constructor de la promesa para indicar que la operación asíncrona ha tenido éxito y devolver un valor.

```javascript
const myPromise = new Promise((resolve, reject) => {
  // Resolver la promesa con un valor
  resolve('Éxito');
});

```
- **`catch`:** Se utiliza para manejar errores o rechazos que ocurren durante la ejecución de una promesa.

```javascript
myPromise.catch((error) => {
  console.error(error); // Output: Error
});

```
## Uso del método every del objeto Promise

El método `every` del objeto Promise se utiliza para verificar si todas las promesas en un iterable se han resuelto correctamente.

```javascript
const promises = [Promise.resolve(true), Promise.reject(false)];

Promise.every(promises)
  .then((result) => {
    console.log(result); // Output: false
  })
  .catch((error) => {
    console.error(error); // Output: false
  });

```

## Throw / Try

Las promesas también pueden lanzar errores utilizando la sintaxis de `throw` y `try`.

```javascript
const myPromise = new Promise((resolve, reject) => {
  try {
    // Lanzar un error
    throw new Error('Error');
  } catch (error) {
    // Rechazar la promesa con el error
    reject(error);
  }
});

```

## El operador await

El operador `await` se utiliza para esperar que una promesa se resuelva antes de continuar con la ejecución del código. Solo puede ser utilizado dentro de funciones marcadas con la palabra clave `async`.

```javascript
async function myFunction() {
  const result = await myPromise;
  console.log(result); // Output: Éxito
}

```

## Cómo utilizar una función async

Las funciones marcadas con la palabra clave `async` devuelven una promesa, lo que permite utilizar la sintaxis `await` dentro de ellas.

```javascript
async function fetchData() {
  try {
    const data = await fetchDataFromAPI();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

```
Estas características de ES6 proporcionan herramientas poderosas para trabajar con operaciones asíncronas de manera más eficiente y legible en JavaScript. Al utilizar promesas y sus métodos asociados, puedes manejar fácilmente el flujo asíncrono y mejorar la legibilidad de tu código.

