const fs = require('fs');
const path = require('path');
const boxen = require('boxen');
const chalk = require('chalk');
const concurrently = require('concurrently');
const { cp, mkdir } = require('shelljs');

const USAGE = `Usage
  $ solve yyyy d[d]`;

let year, day;
try {
  if (process.argv.length != 4) {
    throw new Error();
  }

  [year, day] = process.argv.slice(2).map(arg => arg.padStart(2, '0'));
  if (!/^\d{4}$/.test(year) || !/^\d{2}$/.test(day)) throw new Error();
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
