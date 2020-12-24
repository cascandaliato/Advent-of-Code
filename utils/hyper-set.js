class HyperSet {
  constructor() {
    this._set = new Set();
  }

  has(coords) {
    return this._set.has(coords.join(';'));
  }

  add(coords) {
    this._set.add(coords.join(';'));
  }

  remove(coords) {
    this.delete(coords);
  }

  delete(coords) {
    this._set.delete(coords.join(';'));
  }

  toggle(coords) {
    if (this.has(coords)) this.delete(coords);
    else this.add(coords);
  }

  *[Symbol.iterator]() {
    for (const coords of this._set) {
      yield coords.split(';').map(Number);
    }
  }

  toArray() {
    return [...this._set].map(coords => coords.split(';').map(Number));
  }

  get size() {
    return this._set.size;
  }
}

module.exports = HyperSet;
