# Clases en JavaScript ES6

Este proyecto demuestra el uso de clases en JavaScript según la especificación ES6 (ECMAScript 2015). Las clases proporcionan una forma más clara y orientada a objetos de definir estructuras y jerarquías de objetos en JavaScript.

## Contenido

1. [Introducción](#introducción)
2. [Sintaxis](#sintaxis)
3. [Constructor](#constructor)
4. [Métodos](#métodos)
5. [Herencia](#herencia)
6. [Getter y Setter](#getter-y-setter)

## Introducción

Las clases en JavaScript ES6 son una adición sintáctica que facilita la programación orientada a objetos en JavaScript. Permiten definir plantillas para crear objetos y establecer relaciones de herencia entre ellos.

## Sintaxis

La sintaxis para definir una clase en JavaScript ES6 es la siguiente:

```javascript
class MiClase {
    constructor() {
        // Constructor de la clase
    }

    metodo() {
        // Métodos de la clase
    }
}

```

## Constructor

El método constructor() se utiliza para inicializar los objetos creados a partir de la clase. Es llamado automáticamente cuando se instancia la clase.

## Métodos

Los métodos son funciones definidas dentro de una clase que pueden ser llamadas en las instancias de esa clase.

## Herencia

Las clases en JavaScript admiten herencia mediante la palabra clave 'extends'. Esto permite que una clase hija herede propiedades y métodos de una clase 
padre.

```javascript
class ClaseHija extends ClasePadre {
    constructor() {
        super(); // Llama al constructor de la clase padre
    }

    // Métodos adicionales de la clase hija
}

```
## Getter y Setter

ES6 también introdujo los métodos 'get' y 'set' que se pueden utilizar dentro de una clase para definir propiedades con comportamiento personalizado 
para la lectura y escritura.

```javascript
class Persona {
    constructor(nombre) {
        this._nombre = nombre;
    }

    get nombre() {
        return this._nombre;
    }

    set nombre(nuevoNombre) {
        this._nombre = nuevoNombre;
    }
}

```
Este README proporciona una visión general de cómo utilizar clases en JavaScript ES6 en tus proyectos.Si necesitas más detalles o tienes alguna 
pregunta, no dudes en consultar la documentación oficial de JavaScript.
