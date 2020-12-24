class HyperMap {
  constructor(defaultValue = undefined) {
    this._defaultValue = defaultValue;
    this._map = new Map();
  }

  get(coords) {
    return this._map.get(coords.join(';')) || this._defaultValue;
  }

  set(coords, value) {
    if (value === this._defaultValue) {
      this._map.delete(coords.join(';'));
    } else {
      this._map.set(coords.join(';'), value);
    }
  }

  delete(coords) {
    this._map.delete(coords.join(';'));
  }

  *[Symbol.iterator]() {
    for (const [key, value] of this._map) {
      yield [key.split(';').map(Number), value];
    }
  }

  get size() {
    return this._map.size;
  }
}

module.exports = HyperMap;
