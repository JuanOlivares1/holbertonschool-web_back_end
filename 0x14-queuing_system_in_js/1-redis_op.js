import { redisClientFactory } from 'kue';
import { createClient } from 'redis';

(async () => {
  const client = createClient();

  client.on('error', (err) => console.log('Redis client not connected to the server: ', err));
  client.on('connect', () => console.log('Redis client connected to the server'));

  await client.connect();

  async function setNewSchool(schoolName, value) {
    const reply = await client.set(schoolName, value);
    console.log('Reply: ', reply);
  }
  
  async function displaySchoolValue(schoolName) {
    const name = await client.get(schoolName);
    console.log(name);
  }
  
  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');  
})();
