export default class Currency {
  constructor(code = '', name = '') {
    // Constructor to initialize the code and name of the currency.
    this._code = code;
    this._name = name;
  }

  // Getter and setter for the attribute 'code'.
  get code() {
    return this._code;
  }

  set code(code) {
    this._code = code;
  }

  // Getter and setter for the attribute 'name'.
  get name() {
    return this._name;
  }

  set name(name) {
    this._name = name;
  }

  // Method to display the full currency (name and code)
  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
