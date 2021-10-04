const fs = require('fs');

function countStudents(database) {
  try {
    let data = fs.readFileSync(database, { encoding: 'utf8', flag: 'r' });
    let counter = 0;
    const obj = {};

    data = data.split('\n');

    for (let i = 0; i < data.length; i += 1) {
      data[i] = data[i].split(',');
    }
    for (let i = 1; i < data.length; i += 1) {
      if (data[i].length > 1) {
        counter += 1;
        if (!Object.prototype.hasOwnProperty.call(obj, data[i][data[i].length - 1])) {
          obj[data[i][data[i].length - 1]] = {
            count: 1,
            names: [data[i][0]],
          };
        } else {
          obj[data[i][data[i].length - 1]].count += 1;
          obj[data[i][data[i].length - 1]].names.push(data[i][0]);
        }
      }
    }
    const keys = Object.keys(obj);
    console.log(`Number of students: ${counter}`);

    for (let i = 0; i < keys.length; i += 1) {
      console.log(`Number of students in ${keys[i]}: ${obj[keys[i]].count}. List: ${obj[keys[i]].names.join(', ')}`);
    }
  } catch (e) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;