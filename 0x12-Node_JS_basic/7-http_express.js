const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (req, resp) => {
  resp.send('Hello Holberton School!');
});

app.get('/students', (req, resp) => {
  countStudents(process.argv[2]).then((value) => {
    resp.write('This is the list of our students\n');
    resp.end(value);
  }).catch((err) => {
    resp.write('This is the list of our students\n');
    resp.end(`${err.message}`);
  });
});

app.listen(port, () => {
  console.log(`app listening at http://localhost:${port}/`);
});

module.exports = app;
