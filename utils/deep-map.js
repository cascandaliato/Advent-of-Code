module.exports = class DeepMap {
  constructor(depth) {
    this.map = new Map();
    this.depth = depth;
  }

  get(...args) {
    // if (args.length !== this.depth)
    //   throw new Error(
    //     `Wrong number of args in .get(): expected ${this.depth}, got ${args.length} (args=${args})`
    //   );

    if (this.depth === 1) {
      return this.map.get(...args);
    } else {
      if (this.map.get(args[0]) === undefined) return undefined;
      else return this.map.get(args[0]).get(...args.slice(1));
    }
  }

  set(...args) {
    // if (args.length !== this.depth + 1)
    //   throw new Error(
    //     `Wrong number of args in .set(): expected ${this.depth + 1}, got ${
    //       args.length
    //     } (args=${args})`
    //   );

    if (this.depth === 1) {
      return this.map.set(...args);
    } else {
      if (this.map.get(args[0]) === undefined)
        this.map.set(args[0], new DeepMap(this.depth - 1));
      return this.map.get(args[0]).set(...args.slice(1));
    }
  }

  has(...args) {
    // if (args.length !== this.depth)
    //   throw new Error(
    //     `Wrong number of args in .has(): expected ${this.depth}, got ${args.length} (args=${args})`
    //   );

    if (this.depth === 1) {
      return this.map.has(...args);
    } else {
      if (this.map.get(args[0]) === undefined) return false;
      else return this.map.get(args[0]).has(...args.slice(1));
    }
  }

  toString() {
    const strings = [`DeepMap(depth=${this.depth}) {`];
    for (const [k, v] of this) {
      strings.push(`  ${JSON.stringify(k)} => ${JSON.stringify(v)}`);
    }
    strings.push('}');
    return strings.join('\n');
  }

  *[Symbol.iterator]() {
    if (this.depth === 1) {
      yield* this.map[Symbol.iterator]();
    } else {
      for (const [k, v] of this.map) {
        for (const inmap of v)
          yield [[k, ...inmap.slice(0, -1)], inmap.slice(-1)[0]];
      }
    }
  }

  [Symbol.toStringTag]() {
    return 'DeepMap';
  }
};
