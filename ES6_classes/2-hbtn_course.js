export default class HolbertonCourse {
  constructor (name = '', length = 0, students = []) {
    // validation for the attribute 'name'
    if (typeof name !== 'string') {
      throw new Error('Name must be a string');
    }
    this._name = name;

    // validation for the attribute 'length'
    if (typeof length !== 'number') {
      throw new Error('Length must be a number');
    }
    this._length = length;

    // validation for the attribute 'students'
    if (!Array.isArray(students)) {
      throw new Error('Students must be a array');
    }
    this._students = students;
  }

  // Getter and setter for the attribute 'name'
  get name () {
    return this._name;
  }

  set name (name) {
    if (typeof name !== 'string') {
      throw new Error('Name must be a string');
    }
    this._name = name;
  }

  // Getter and setter fro the attribute 'length'
  get length () {
    return this._length;
  }

  set length (length) {
    if (typeof length !== 'number') {
      throw new Error('Length must be a number');
    }
    this._length = length;
  }

  // Getter and setter fro the attribute 'students'
  get students () {
    return this._students;
  }

  set students (students) {
    if (!Array.isArray(students)) {
      throw new Error('Students must be a array');
    }
    this._students = students;
  }
}
