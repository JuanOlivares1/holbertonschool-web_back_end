import { createClient } from 'redis';

(async () => {
  const client = createClient();

  client.on('error', (err) => console.log('Redis client not connected to the server: ', err));
  client.on('connect', () => console.log('Redis client connected to the server'));

  await client.connect();

  async function setNewSchool(schoolName, value) {
    console.log(`Reply: ${await client.set(schoolName, value)}`);
  }

  async function displaySchoolValue(schoolName) {
    console.log(await client.get(schoolName));
  }

  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
})();
