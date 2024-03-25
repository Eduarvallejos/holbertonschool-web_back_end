// Car class definition
export default class Car {
  constructor(brand = '', motor = '', color = '') {
    // Constructor to initialize the _brand, _motor, and _color attributes
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Getter for the _brand attribute
  get brand() {
    return this._brand;
  }

  // Getter for the _motor attribute
  get motor() {
    return this._motor;
  }

  // Getter for the _color attribute
  get color() {
    return this._color;
  }

  cloneCar() {
    // Method to clone a Car object
    const newCar = new Car(this._brand, this._motor, this._color); // Copiar los valores de atributos
    // Set the prototype of the new object
    Object.setPrototypeOf(newCar, Object.getPrototypeOf(this));
    return newCar; // Return the cloned new object
  }
}
