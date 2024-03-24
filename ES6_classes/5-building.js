export default class Building {
  constructor(sqft = 0) {
    // Check if the instance is not directly of the abstract class Building
    // And if the subclass has not implemented the evacuationWarningMessage method
    if (this.constructor !== Building && this.evacuationWarningMessage === undefined) {
      // If the method is not implemented, an error is thrown
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    this._sqft = sqft;
  }

  // Getter for the 'sqft' attribute.
  get sqft() {
    return this._sqft;
  }
}
