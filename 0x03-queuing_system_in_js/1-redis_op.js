import { createClient } from 'redis';
const redis = require('redis');

const redisClient = createClient();

redisClient.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

redisClient.on('ready', () => console.log('Redis client connected to the server '));

function setNewSchool(schoolName, value) {
  redisClient.set(schoolName, value, redis.print)
}

function displaySchoolValue(schoolName) {
  (redisClient.get(schoolName, (err, res) => {
    if (err) {
      console.log(err.message);
    } else {
      console.log(res);
    }
  }));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
