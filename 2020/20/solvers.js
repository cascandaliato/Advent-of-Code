const { getCol, splitByBlankLine } = require('../../utils');
const { cloneDeep } = require('lodash');

const symbols = { '.': 0, '#': 1 };

exports.normalizeInput = lines =>
  splitByBlankLine(lines).map(tile => ({
    id: Number(tile[0].slice(0, -1).split(' ')[1]),
    image: tile.slice(1).map(row => [...row].map(ch => symbols[ch])),
  }));

const otherSide = {
  north: 'south',
  south: 'north',
  east: 'west',
  west: 'east',
};

const getSide = {
  north: ({ image }) => parseInt(image[0].join(''), 2),
  south: ({ image }) => parseInt(image[image.length - 1].join(''), 2),
  east: ({ image }) => parseInt(getCol(image, image[0].length - 1).join(''), 2),
  west: ({ image }) => parseInt(getCol(image, 0).join(''), 2),
};

const baseTransforms = {
  flipV: ({ id, image }) => ({
    id,
    image: cloneDeep(image).map((row, rIdx) =>
      row.map((_, cIdx) => image[rIdx][row.length - 1 - cIdx])
    ),
  }),
  flipH: ({ id, image }) => ({
    id,
    image: cloneDeep(image).map((row, rIdx) =>
      row.map((_, cIdx) => image[image.length - 1 - rIdx][cIdx])
    ),
  }),
  rotateCW: ({ id, image }) => ({
    id,
    image: cloneDeep(image).map((row, rIdx) =>
      row.map((_, cIdx) => {
        const adjCol = cIdx - (row.length - 1);
        const [origRow, origCol] = [-adjCol, rIdx];
        return image[origRow][origCol];
      })
    ),
  }),
};

const transforms = {
  none: [],
  fH: [baseTransforms.flipH],
  fV: [baseTransforms.flipV],
  'fH-fV': [baseTransforms.flipH, baseTransforms.flipV],
  rCW: [baseTransforms.rotateCW],
  rCWx3: [
    baseTransforms.rotateCW,
    baseTransforms.rotateCW,
    baseTransforms.rotateCW,
  ],
  'fV-rCW': [baseTransforms.flipV, baseTransforms.rotateCW],
  'fH-rCW': [baseTransforms.flipH, baseTransforms.rotateCW],
};

const applyTransform = (transform, tile) =>
  transforms[transform].reduce((newTile, baseT) => {
    return { ...baseT(newTile), transform };
  }, tile);

const transformMap = (transform, map) =>
  applyTransform(transform, {
    image: map,
  }).image;

const findSidesThatLineUp = (tile, bySide) =>
  Object.keys(getSide).filter(
    side =>
      bySide
        .get(otherSide[side])
        .get(getSide[side](tile))
        // exclude self
        .filter(({ id }) => id !== tile.id).length > 0
  );

const organizeTiles = tiles => {
  const bySide = new Map([
    ['north', new Map()],
    ['south', new Map()],
    ['east', new Map()],
    ['west', new Map()],
  ]);

  for (const tile of tiles) {
    for (const transform in transforms) {
      const transformed = applyTransform(transform, tile);
      for (const side in getSide) {
        const value = getSide[side](transformed);
        if (!bySide.get(side).has(value)) bySide.get(side).set(value, []);
        bySide.get(side).get(value).push(transformed);
      }
    }
  }

  const corners = tiles.filter(
    tile => findSidesThatLineUp(tile, bySide).length === 2
  );

  return { bySide, corners };
};

exports.solveOne = tiles =>
  organizeTiles(tiles)
    .corners.map(({ id }) => id)
    .reduce((a, b) => a * b);

exports.solveTwo = tiles => {
  const { bySide, corners } = organizeTiles(tiles);

  const assembleGridFrom = upperLeftCorner => {
    const gridLen = Math.sqrt(tiles.length);
    const tmpGrid = Array.from({ length: gridLen }, () =>
      Array.from({ length: gridLen }, () => 0)
    );

    tmpGrid[0][0] = upperLeftCorner;
    for (let row = 0; row < tmpGrid.length; row++) {
      for (let col = 0; col < tmpGrid[0].length; col++) {
        if (row === 0 && col === 0) continue;
        if (row === 0) {
          tmpGrid[row][col] = bySide
            .get('west')
            .get(getSide.east(tmpGrid[row][col - 1]))
            .filter(
              ({ id: otherId }) => otherId !== tmpGrid[row][col - 1].id
            )[0];
        } else {
          tmpGrid[row][col] = bySide
            .get('north')
            .get(getSide.south(tmpGrid[row - 1][col]))
            .filter(({ id }) => id !== tmpGrid[row - 1][col].id)[0];
        }
      }
    }
    return tmpGrid;
  };

  let grid;

  for (const transform in transforms) {
    const transformed = applyTransform(transform, corners[0]);
    const sides = findSidesThatLineUp(transformed, bySide);
    // look for upper-left corner
    if (sides.includes('east') && sides.includes('south')) {
      grid = assembleGridFrom(transformed);
      break;
    }
  }

  // remove borders
  for (const row of grid) {
    for (const tile of row) {
      tile.image = tile.image
        .slice(1, -1)
        .map(imageRow => imageRow.slice(1, -1));
    }
  }

  const newTileLen = tiles[0].image.length - 2;
  const mapLen = Math.sqrt(tiles.length) * newTileLen;
  const map = Array.from({ length: mapLen }, () =>
    Array.from({ length: mapLen }, () => 0)
  ).map((row, rIdx) =>
    row.map((_, cIdx) => {
      const gridRow = Math.floor(rIdx / newTileLen);
      const gridCol = Math.floor(cIdx / newTileLen);
      const imageRow = rIdx % newTileLen;
      const imageCol = cIdx % newTileLen;
      return grid[gridRow][gridCol].image[imageRow][imageCol];
    })
  );

  const dragon = `
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   `
    .split('\n')
    .slice(1)
    .flatMap((line, rIdx) => line.split('').map((v, cIdx) => [v, [rIdx, cIdx]]))
    .filter(([val]) => val === '#')
    .map(([_, coords]) => coords);
  const dragonW =
    dragon.map(([_, col]) => col).reduce((a, b) => Math.max(a, b)) + 1;
  const dragonH =
    dragon.map(([row]) => row).reduce((a, b) => Math.max(a, b)) + 1;

  const markDragons = m => {
    for (let rIdx = 0; rIdx + dragonH - 1 < m.length; rIdx++) {
      for (let cIdx = 0; cIdx + dragonW - 1 < m[0].length; cIdx++) {
        if (dragon.every(([dR, dC]) => m[rIdx + dR][cIdx + dC] >= 1)) {
          dragon.forEach(([dR, dC]) => (m[rIdx + dR][cIdx + dC] += 1));
        }
      }
    }
  };

  const countOctothorpes = m =>
    m.flatMap(row => row.filter(v => v === 1)).reduce((a, b) => a + b);

  const initialOctothorpesCount = countOctothorpes(map);

  for (const transform in transforms) {
    const transformed = transformMap(transform, map);
    markDragons(transformed);
    const newOctothorpesCount = countOctothorpes(transformed);
    if (newOctothorpesCount !== initialOctothorpesCount)
      return newOctothorpesCount;
  }
};
