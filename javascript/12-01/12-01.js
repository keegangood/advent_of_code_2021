let data = require("./data.json");

const part1 = data.filter((datum, i, arr) => arr[i] > arr[i - 1]).length;
// console.log(part1) // 1676

const part2 = data.filter(
  (_, i, arr) =>
    arr.slice(i + 1, i + 4).reduce((x, y) => x + y, 0) >
    arr.slice(i, i + 3).reduce((x, y) => x + y, 0)
).length;
// console.log(part2) // 1706
