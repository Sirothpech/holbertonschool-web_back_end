export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof newName === "string") {
      this._name = newName;
    } else {
      throw new Error("Name must be a string");
    }
  }

  get length() {
    return this._length;
  }

  set length(newLength) {
    if (typeof newLength === "string") {
      this._length = newLength;
    } else {
      throw new Error("Length must be a number");
    }
  }

  get students() {
    return this._students;
  }

  set students(newStudents) {
    if (Array.isArray(newStudents) && newStudents.every((student) => typeof student === 'string')) {
      this._students = newStudents;
    } else {
      throw new Error("Students must be a array of Strings");
    }
  }
}
