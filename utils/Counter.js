exports.Counter = class Counter extends Map {
  constructor(iter = []) {
    super();
    for (const key of iter) {
      this.increment(key);
    }
  }

  increment(key) {
    if (this.has(key)) {
      this.set(key, this.get(key) + 1);
    } else {
      this.set(key, 1);
    }
  }

  decrement(key) {
    if (!this.has(key)) throw new Error(`Invalid key ${key}`);
    this.set(key, this.get(key) - 1);
    if (this.get(key) === 0) this.delete(key);
  }
};
