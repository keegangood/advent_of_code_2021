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

console.log(part1(data))
