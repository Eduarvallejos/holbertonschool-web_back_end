// HolbertonClass class definition
export default class HolbertonClass {
  constructor(size = 0, location = '') {
    // Constructor initializes the _size and _location attributes
    this._size = size;
    this._location = location;
  }

  valueOf() {
    // Overrides the valueOf method to convert the instance to a number
    return this._size;
  }

  toString() {
    // Overrides the toString method to convert the instance to a string
    return this._location;
  }
}
