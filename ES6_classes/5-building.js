export default class Building {
  constructor(sqft) {
    this._sqft = sqft;
}

  get sqft() {
    return this._sqft;
  }

  set sqft(newSqft) {
    if (typeof newSqft === 'number') {
      this._sqft = newSqft;
    } else {
      throw new TypeError('Sqft must be a number');
    }
  }

  evacuationWarningMessage() {
    return `Class extending Building must override ${this.constructor.name}`;
  }
}
