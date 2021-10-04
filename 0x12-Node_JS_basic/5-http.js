const http = require('http');
const countStudents = require('./3-read_file_async');

const hostname = '127.0.0.1';
const port = 1245;

const app = http.createServer((req, resp) => {
  resp.statusCode = 200;
  resp.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    resp.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    countStudents(process.argv[2]).then((value) => {
      resp.write('This is the list of our students\n');
      resp.end(value);
    }).catch((err) => {
      resp.write('This is the list of our students\n');
      resp.end(`${err.message}`);
    });
  } else {
    resp.end();
  }
});

app.listen(port, hostname, () => {
  console.log('Welcome!');
});

module.exports = app;
