export default class HolbertonClass {
  constructor(size, location) {
    this.size = size;
    this.location = location;
  }

  valueOf() {
    return this.size;
  }

  toString() {
    return this.location;
  }
}
