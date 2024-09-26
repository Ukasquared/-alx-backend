import { createClient } from 'redis';
const redis = require('redis');

const redisClient = createClient();

redisClient.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

redisClient.on('ready', () => console.log('Redis client connected to the server '));

redisClient.subscribe('holberton school channel', (err) => {
    if (err) {
        console.log(err.message);
    }
});

redisClient.on('message', (channel, msg) => {

    if (msg === 'KILL_SERVER') {
        redisClient.unsubscribe(channel, () => {
            redisClient.quit();
        });
    }
    console.log(msg);
});


