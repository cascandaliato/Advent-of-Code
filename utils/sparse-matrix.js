const DeepMap = require('./deep-map');

module.exports = class SparseMatrix extends DeepMap {
  constructor(arrOfArrs) {
    super(2);

    this.numRows = arrOfArrs.length;
    this.numCols = arrOfArrs[0].length;

    arrOfArrs.forEach((row, rIdx) =>
      row.forEach((v, cIdx) => this.set(rIdx, cIdx, v))
    );
  }
};
