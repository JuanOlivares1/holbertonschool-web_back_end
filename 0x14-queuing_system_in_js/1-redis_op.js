import { createClient } from 'redis';

(async () => {
  const client = createClient();

  client.on('error', (err) => console.log('Redis client not connected to the server: ', err));
  client.on('connect', () => console.log('Redis client connected to the server'));

  await client.connect();

  function setNewSchool(schoolName, value) {
    client.set(schoolName, value)
      .then(res => console.log(`Reply: ${res}`))
      .catch(err => console.log(err));
  }

  function displaySchoolValue(schoolName) {
    client.get(schoolName)
      .then(res => console.log(res))
      .catch(err => console.log(err));
  }

  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
})();
