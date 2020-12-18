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
    this._set.remove(coords.join(';'));
  }

  *[Symbol.iterator]() {
    for (const coords of this._set) {
      yield coords.split(';').map(Number);
    }
  }
  getPopulated() {
    return [...this._set].map(coords => coords.split(';').map(Number));
  }
}

module.exports = HyperSet;
