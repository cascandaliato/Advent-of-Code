exports.parse = lines => {
  const passports = [];

  let passport = {};
  for (const line of lines) {
    if (!line) {
      passports.push(passport);
      passport = {};
      continue;
    }

    const partial = line
      .split(' ')
      .reduce(
        (acc, kV) => ({ ...acc, [kV.split(':')[0]]: kV.split(':')[1] }),
        {}
      );

    passport = { ...passport, ...partial };
  }

  passports.push(passport);

  return passports;
};

exports.solveOne = input =>
  input.filter(p =>
    ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'].every(f => f in p)
  ).length;

const validations = {
  byr: v => /^\d{4}$/.test(v) && Number(v) >= 1920 && Number(v) <= 2002,
  iyr: v => /^\d{4}$/.test(v) && Number(v) >= 2010 && Number(v) <= 2020,
  eyr: v => /^\d{4}$/.test(v) && Number(v) >= 2020 && Number(v) <= 2030,
  hgt: v => {
    const match = v.match(/^(\d+)(cm|in)$/);
    if (!match) return false;
    const height = match[1];
    const unit = match[2];
    return unit === 'cm'
      ? height >= 150 && height <= 193
      : height >= 59 && height <= 76;
  },
  hcl: v => /^#[0-9a-f]{6}$/.test(v),
  ecl: v => ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'].includes(v),
  pid: v => /^\d{9}$/.test(v),
};

exports.solveTwo = input =>
  input.filter(p =>
    Object.keys(validations).every(f => f in p && validations[f](p[f]))
  ).length;
