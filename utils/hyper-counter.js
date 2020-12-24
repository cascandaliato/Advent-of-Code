const HyperMap = require('./hyper-map');
class HyperCounter {
  constructor() {
    this._map = new HyperMap(0);
  }

  get(coords) {
    return this._map.get(coords);
  }

  add(coords) {
    this._map.set(coords, this._map.get(coords) + 1);
  }

  remove(coords) {
    const current = this._map.get(coords);
    if (current === 1) {
      this._map.delete(coords);
    } else {
      this._map.set(coords, current - 1);
    }
  }

  *[Symbol.iterator]() {
    yield* this._map[Symbol.iterator]();
  }
}

module.exports = HyperCounter;
