const { entries, fromPairs, max, values } = require('lodash');

exports.normalizeInput = lines =>
  lines.map(line => {
    const tokens = line.split(' ');
    return {
      reindeer: tokens[0],
      speed: Number(tokens[3]),
      time: Number(tokens[6]),
      rest: Number(tokens[tokens.length - 2]),
    };
  });

const distancesAfterSec = (timeSec, reindeers) =>
  reindeers.reduce((byReindeer, { reindeer, speed, time, rest }) => {
    const factor = Math.floor(timeSec / (time + rest));
    const remainder = timeSec % (time + rest);
    byReindeer[reindeer] =
      factor * speed * time + Math.min(remainder, time) * speed;
    return byReindeer;
  }, {});

const maxDistanceAfterSec = timeSec => reindeers =>
  values(distancesAfterSec(timeSec, reindeers)).reduce((a, b) =>
    Math.max(a, b)
  );

exports.maxDistanceAfterSec = maxDistanceAfterSec;

exports.solveOne = maxDistanceAfterSec(2503);

const maxPointsAfterSec = timeSec => reindeers => {
  const points = fromPairs(reindeers.map(({ reindeer }) => [reindeer, 0]));

  for (let sec = 1; sec <= timeSec; sec++) {
    const distances = distancesAfterSec(sec, reindeers);
    const maxDistance = max(values(distances));
    entries(distances)
      .filter(([, distance]) => distance === maxDistance)
      .forEach(([reindeer]) => points[reindeer]++);
  }

  return max(values(points));
};

exports.maxPointsAfterSec = maxPointsAfterSec;

exports.solveTwo = maxPointsAfterSec(2503);
