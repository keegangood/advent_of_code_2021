let data = require('./data.json')

const part1 = data => {
  let position = {
    forward: 0,
    depth: 0
  }

  data.forEach(move => {
    let [direction, distance] = move.split(' ')
    distance = parseInt(distance)

    switch (direction) {
      case 'forward':
        position.forward += distance
        break
      case 'up':
        position.depth -= distance
        break
      case 'down':
        position.depth += distance
        break
    }
  })

  return position.depth * position.forward
}

// console.log(part1(data)) // 1714680

const part2 = data => {
  let position = {
    aim: 0,
    forward: 0,
    depth: 0
  }

  data.forEach(move => {
    let [direction, value] = move.split(' ')
    value = parseInt(value)

    switch (direction) {
      case 'forward':
        position.forward += value
        position.depth += position.aim * value
        break
      case 'up':
        position.aim -= value
        break
      case 'down':
        position.aim += value
        break
      default:
        break
    }
  })

  return position.depth * position.forward
}

// console.log(part2(data)) // 1963088820
