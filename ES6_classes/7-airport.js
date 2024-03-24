// Airport class definition
export default class Airport {
  constructor(name = '', code = '') {
    // Initialize name and code attributes
    this._name = name;
    this._code = code;
  }

  // toString method definition
  toStringTag() {
    // Returns a string representation of the Airport objec
    return `[objeto ${this._code}]`;
  }
}
