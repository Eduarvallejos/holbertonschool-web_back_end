// Import the 'Building' class from 5-building.js
import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft = Building, floors = 0) {
    // Call the constructor of the Building class using super() to initialize the 'sqft' attribute
    super(sqft);
    // Initialize the 'floors' attribute specific to this class
    this._floors = floors;
  }

  // Getter for the 'floors' attribute.
  get floors() {
    return this._floors;
  }

  // Implementation of the evacuationWarningMessage method overriding the
  // one from the Building class
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
