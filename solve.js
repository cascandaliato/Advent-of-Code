const fs = require('fs');
const path = require('path');
const chalk = require('chalk');
const concurrently = require('concurrently');
const { cp, mkdir } = require('shelljs');

const USAGE = `Usage
  $ solve yyyy d
where
  2015 <= yyyy <= ${new Date().getFullYear()}
  1 <= d <= 25
`;

const validate = (y, d) => {
  if (
    !/^\d{4}$/.test(y) ||
    Number(y) < 2015 ||
    Number(y) > new Date().getFullYear() ||
    !/^\d{2}$/.test(d) ||
    Number(d) > 25
  )
    throw new Error();
};

let year = new Date().getFullYear().toString();
let day = new Date().getDate().toString();

try {
  switch (process.argv.length) {
    case 2:
      break;
    case 3:
      // past year
      if (year !== process.argv[2]) day = '01';
      year = process.argv[2];
      break;
    case 4:
      [year, day] = process.argv.slice(2);
      break;
    default:
      throw new Error();
  }

  day = day.padStart(2, '0');
  validate(year, day);
} catch (_) {
  console.log(USAGE);
  return -1;
}

const template = path.join(__dirname, 'template', '*');
const targetDir = path.join(__dirname, year, day);
if (!fs.existsSync(targetDir)) {
  mkdir('-p', targetDir);
  cp('-R', template, targetDir);
}

console.log(chalk`Preparing y{greenBright ${year}} d{greenBright ${day}}...\n`);

const pattern = path.join(year, day);
concurrently(
  [
    {
      command: `npx nodemon --watch ${pattern} --watch utils -e "*" --exec "npx jest ${year}/${day}"`,
      name: 'test',
    },
    {
      command: `npx nodemon --watch ${pattern} --watch utils -e "*" "${pattern}"`,
      name: 'main',
    },
  ],
  { prefix: '[{time} {name}]', timestampFormat: 'HH:mm:ss' }
);
