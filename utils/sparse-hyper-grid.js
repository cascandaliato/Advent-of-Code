const { multiRange } = require('.');

module.exports = class SparseHyperMatrix {
  constructor({
    initialValue = [],
    defaultValue = undefined,
    separator = ',',
  } = {}) {
    this.initialValue = initialValue;
    this.defaultValue = defaultValue;
    this.separator = separator;
    this.map = new Map(initialValue);
  }

  get(...args) {
    return this.map.get(args.join(this.separator)) || this.defaultValue;
  }

  set(...args) {
    const key = args.slice(0, -1).join(this.separator);
    const value = args.slice(-1)[0];
    this.map.set(key, value);
  }

  getBoundaries() {
    const boundaries = Array.from(
      { length: [...this.map][0][0].split(this.separator).length },
      () => [+Infinity, -Infinity]
    );

    for (const [coords, value] of this.map) {
      if (value != this.defaultValue) {
        coords
          .split(this.separator)
          .map(Number)
          .forEach((coord, idx) => {
            if (coord < boundaries[idx][0]) boundaries[idx][0] = coord;
            if (coord > boundaries[idx][1]) boundaries[idx][1] = coord;
          });
      }
    }

    return boundaries;
  }

  clone() {
    return new SparseHyperMatrix({
      initialValue: [...this.map].filter(
        entry => entry.slice(-1)[0] !== this.defaultValue
      ),
      defaultValue: this.defaultValue,
      separator: this.separator,
    });
  }

  *[Symbol.iterator]() {
    for (const [coords, value] of this.map) {
      yield [...coords.split(this.separator).map(Number), value];
    }
  }

  print(map = v => v) {
    const [[xMin, xMax], [yMin, yMax], ...rest] = this.getBoundaries();
    for (const k of multiRange(rest)) {
      console.log(...k.map((v, idx) => `d${idx + 3}=${v}`));
      for (let row = yMin; row <= yMax; row++) {
        let line = '';
        for (let col = xMin; col <= xMax; col++) {
          line += map(this.get(col, row, ...k));
        }
        console.log(line);
      }
      console.log();
    }
  }
};
