export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    } else if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    } else if (Array.isArray(students) === false) {
      throw new TypeError('Students must be an array of strings');
    } else if (students.every((i) => (typeof i === 'string')) !== true) {
      throw new TypeError('Students must be an array of strings');
    }

    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(val) {
    if (typeof val !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = val;
  }

  get length() {
    return this._length;
  }

  set length(val) {
    if (typeof value !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = val;
  }

  get students() {
    return this._students;
  }

  set students(val) {
    if (Array.isArray(val) === false) {
      throw new TypeError('Students must be an array of strings');
    } else if (val.every((i) => (typeof i === 'string')) !== true) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = val;
  }
}
