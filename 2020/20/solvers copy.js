const { splitByBlankLine } = require('../../utils');
const { cloneDeep } = require('lodash');

const symbols = { '.': 0, '#': 1 };

const printMap = map => {
  console.log('\n\n===\nMAP\n===\n');
  for (const row of map) {
    console.log(row.join('').replace(/0/g, '.').replace(/1/g, '#'));
  }
  console.log();
};

const otherSide = {
  north: 'south',
  south: 'north',
  east: 'west',
  west: 'east',
};

const sides = {
  north: ({ image }) => parseInt(image[0].join(''), 2),
  south: ({ image }) => parseInt(image[image.length - 1].join(''), 2),
  east: ({ image }) => {
    const side = [];
    for (const row of image) {
      side.push(row[row.length - 1]);
    }
    return parseInt(side.join(''), 2);
  },
  west: ({ image }) => {
    const side = [];
    for (const row of image) {
      side.push(row[0]);
    }
    return parseInt(side.join(''), 2);
  },
};

const baseTransforms = {
  flipV: ({ id, originalImage, image }) => {
    const newImage = Array.from({ length: originalImage.length }, () =>
      Array(originalImage.length).fill(0)
    ).map((row, rIdx) =>
      row.map((_, cIdx) => image[rIdx][row.length - 1 - cIdx])
    );
    return { id, originalImage, image: newImage };
  },
  flipH: ({ id, originalImage, image }) => {
    const newImage = Array.from({ length: originalImage.length }, () =>
      Array(originalImage.length).fill(0)
    ).map((row, rIdx) =>
      row.map((_, cIdx) => image[originalImage.length - 1 - rIdx][cIdx])
    );
    return { id, originalImage, image: newImage };
  },
  rotateCW: ({ id, originalImage, image }) => {
    const newImage = Array.from({ length: originalImage.length }, () =>
      Array(originalImage.length).fill(0)
    ).map((row, rIdx) =>
      row.map((_, cIdx) => {
        const adjCol = cIdx - (row.length - 1);
        const [origRow, origCol] = [-adjCol, rIdx];
        return image[origRow][origCol];
      })
    );
    return { id, originalImage, image: newImage };
  },
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

exports.normalizeInput = lines =>
  splitByBlankLine(lines).map(tile => {
    const id = Number(tile[0].slice(0, -1).split(' ')[1]);
    const originalImage = tile
      .slice(1)
      .map(row => [...row].map(ch => symbols[ch]));
    const image = tile.slice(1).map(row => [...row].map(ch => symbols[ch]));
    return { id, originalImage, image, transform: 'none' };
  });

const prettyPrintTile = ({ id, image, transform = 'none' }) => {
  console.log();
  console.log(`Tile ${id} [${transform}]`);
  for (const row of image) {
    console.log(row.join('').replace(/0/g, '.').replace(/1/g, '#'));
  }
  console.log();
};

const applyTransform = (transform, tile) =>
  transforms[transform].reduce((newTile, baseT) => {
    return { ...baseT(newTile), transform };
  }, tile);

const prettyPrintGrid = grid => {
  console.log('\n=== GRID ===');
  for (const row of grid) {
    console.log(
      row
        .map(({ id, transform }) => `${id}_${transform.padStart(6, '_')}`)
        .join(' ')
    );
  }
  console.log();
};

exports.solveOne = tiles => {
  console.log('numTiles', tiles.length);
  console.log('gridSide', Math.sqrt(tiles.length));
  console.log('side', Math.sqrt(tiles.length) * (10 - 8));
  console.log(
    'cells',
    Math.sqrt(tiles.length) * (10 - 8) * Math.sqrt(tiles.length) * (10 - 8)
  );

  const byIdAndTransform = new Map();
  tiles.forEach(({ id }) => byIdAndTransform.set(id, new Map()));
  // console.log(byIdAndTransform);

  const bySides = new Map([
    ['north', new Map()],
    ['south', new Map()],
    ['east', new Map()],
    ['west', new Map()],
  ]);
  // console.log(bySides);

  for (const tile of tiles) {
    for (const transform in transforms) {
      const transformed = applyTransform(transform, tile);
      byIdAndTransform.get(tile.id).set(transform, transformed);
      for (const side in sides) {
        const value = sides[side](transformed);
        // if (isNaN(value)) {
        // prettyPrintTile(tile);
        // console.log(tile);
        // console.log(side, tile.id, transform);
        // return;
        // }
        if (!bySides.get(side).has(value)) bySides.get(side).set(value, []);
        bySides.get(side).get(value).push(transformed);
      }
    }
  }

  const corners = [];
  for (const tile of tiles) {
    const matches = [];
    const good = [];
    for (const side in sides) {
      if (
        bySides
          .get(otherSide[side])
          .get(sides[side](tile))
          .filter(({ id }) => id !== tile.id).length === 0
      ) {
        matches.push(side);
      } else {
        good.push([
          side,
          bySides
            .get(otherSide[side])
            .get(sides[side](tile))
            .filter(({ id }) => id !== tile.id)[0].id,
        ]);
      }
    }
    if (matches.length === 2) {
      console.log(tile.id, 'bad sides', matches);
      console.log(tile.id, 'good sides', good);
      corners.push(tile);
    }
  }

  console.log(
    corners.length,
    corners.map(({ id, transform }) => `${id}_${transform}`),
    corners.map(({ id }) => id).reduce((a, b) => a * b)
  );

  //===================PART 2

  const tryGrid = (cId, cTransform) => {
    try {
      const newGrid = Array.from({ length: Math.sqrt(tiles.length) }, () =>
        Array(Math.sqrt(tiles.length)).fill(tiles[0])
      );

      newGrid[0][0] = byIdAndTransform.get(cId).get(cTransform);
      for (let row = 0; row < newGrid.length; row++) {
        for (let col = 0; col < newGrid[0].length; col++) {
          if (row === 0 && col === 0) continue;
          if (row === 0) {
            const matches = bySides
              .get('west')
              .get(sides.east(newGrid[row][col - 1]))
              .filter(({ id }) => id !== newGrid[row][col - 1].id);
            if (matches.length > 1 || matches.length === 0) {
              console.log(
                cId,
                cTransform.padEnd(6, ' '),
                'PROBLEMO',
                row,
                col,
                matches
              );
              console.log('error while trying to fill row', row, 'col', col);
              prettyPrintGrid(newGrid);
              return false;
            }
            newGrid[row][col] = bySides
              .get('west')
              .get(sides.east(newGrid[row][col - 1]))
              .filter(
                ({ id: otherId }) => otherId !== newGrid[row][col - 1].id
              )[0];
          } else {
            const matches = bySides
              .get('north')
              .get(sides.south(newGrid[row - 1][col]))
              .filter(({ id }) => id !== newGrid[row - 1][col].id);
            if (matches.length > 1 || matches.length === 0) {
              console.log(
                cId,
                cTransform.padEnd(6, ' '),
                'PROBLEMO',
                row,
                col,
                matches
              );
              console.log('error while trying to fill row', row, 'col', col);
              prettyPrintGrid(newGrid);
              return false;
            }
            newGrid[row][col] = matches[0];
          }
        }
      }
      return newGrid;
    } catch (e) {
      console.log('ERRORE', cId, cTransform, e);
      return false;
    }
  };

  let grid;
  // console.log(corners);
  // console.log(tile.id, tile.transform);
  outer: for (const tile of corners.slice(0, 1)) {
    for (const transform in transforms) {
      // if (!['fV', 'rCWx3'].includes(transform)) continue;
      const transformed = applyTransform(transform, tile);
      // console.log(tile.id, transformed.id, transformed.transform);
      const tmp = tryGrid(transformed.id, transformed.transform);
      if (tmp) {
        console.log(
          transformed.id,
          transformed.transform.padEnd(6, ' '),
          '>>> TRUE <<<'
        );
        grid = tmp;
        // prettyPrintGrid(grid);
        break outer;
      }
    }
  }
  prettyPrintGrid(grid);

  const noBorders = grid.map(row =>
    row.map(tile => {
      tile.image = tile.image
        .slice(1, -1)
        .map(imageRow => imageRow.slice(1, -1));
      return tile;
    })
  );

  // for (const row of noBorders) {
  //   for (const tile of row) {
  //     prettyPrintTile(tile);
  //   }
  // }

  // console.log('NO BORDERS');
  // prettyPrintGrid(noBorders);

  const newTileLen = tiles[0].originalImage.length - 2;
  console.log({ newTileLen });
  const mapSide = Math.sqrt(tiles.length) * (tiles[0].originalImage.length - 2);
  console.log(mapSide);
  const map = Array.from({ length: mapSide }, () =>
    Array.from({ length: mapSide }, () => 0)
  ).map((row, rIdx) =>
    row.map((_, cIdx) => {
      const gridRow = Math.floor(rIdx / newTileLen);
      const imageRow = rIdx % newTileLen;
      const gridCol = Math.floor(cIdx / newTileLen);
      const imageCol = cIdx % newTileLen;
      // console.log(rIdx, gridRow, imageRow, gridCol, imageCol);
      return grid[gridRow][gridCol].image[imageRow][imageCol];
    })
  );
  // //   .map((row, rIdx) =>
  // //   grid[rIdx + 1].map(({ image }) => image[rIdx].join(''))
  // // );
  printMap(map);

  let dragon = `
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   `;
  const dragonW = dragon.split('\n').slice(1)[0].length;
  const dragonH = 3;
  dragon = dragon
    .split('\n')
    .slice(1)
    .flatMap((line, rIdx) => line.split('').map((v, cIdx) => [v, [rIdx, cIdx]]))
    .filter(([v, coords]) => v === '#')
    .map(([v, coords]) => coords);
  console.log(dragon, dragonW, dragonH);
  // console.log(map);
  const countDragons = m => {
    let count = [];
    for (let rIdx = 0; rIdx + dragonH - 1 < m.length; rIdx++) {
      for (let cIdx = 0; cIdx + dragonW - 1 < m[0].length; cIdx++) {
        // console.log(rIdx, cIdx);
        if (dragon.every(([dR, dC]) => m[rIdx + dR][cIdx + dC] >= 1)) {
          dragon.forEach(([dR, dC]) => (m[rIdx + dR][cIdx + dC] += 1));
          count.push([rIdx, cIdx]);
        }
      }
    }
    return count;
  };

  const transformMap = (transform, m) =>
    applyTransform(transform, {
      id: 42,
      originalImage: m,
      image: m,
      transform: 'none',
    }).image;

  for (const transform in transforms) {
    const transformed = transformMap(transform, cloneDeep(map));
    console.log('prima');
    // printMap(transformed);
    countDragons(transformed);
    console.log(
      transform,
      transformed
        .map(row => row.filter(v => v <= 1).reduce((a, b) => a + b))
        .reduce((a, b) => a + b)
    );
  }
};

exports.solveTwo = input => {};
