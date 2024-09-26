import { createClient } from "redis";
const redis = require('redis')

const redisClient = createClient();

redisClient.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

redisClient.on('ready', () => console.log('Redis client connected to the server '));

function hset(key, value) {
    redisClient.hset('HolbertonSchools', key, value, redis.print)
}

const items = {
    Portland : 50,
    Seattle : 80,
    'New York' : 20,
    Bogota : 20,
    Cali : 40,
    Paris : 2
};

for (const key in items) {
    hset(key, items[key]);
}

redisClient.hgetall('HolbertonSchools', (err, reply) => {
    if (err) {
        console.log(err.msg);
    } else {
        console.log(reply);
    }
});