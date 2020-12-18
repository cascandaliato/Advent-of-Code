class HyperCounter {
  constructor() {
    this._map = new Map();
  }

  get(coords) {
    return this._map.get(coords.join(';')) || 0;
  }

  add(coords) {
    this._map.set(coords.join(';'), this.get(coords) + 1);
  }

  remove(coords) {
    const current = this.get(coords);
    if (current === 1) {
      this._map.remove(coords.join(';'));
    } else {
      this._map.set(coords.join(';'), current - 1);
    }
  }

  *[Symbol.iterator]() {
    for (const [key, value] of this._map) {
      yield [key.split(';'), value];
    }
  }
}

module.exports = HyperCounter;
