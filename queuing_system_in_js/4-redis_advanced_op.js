import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => console.log('Redis client connected to the server'));

client.on('error', (error) => console.log(`Redis client not connected to the server: ${error}`));

// Utilisez une boucle pour insérer chaque paire clé-valeur
const datas = {
    Portland: '50',
    Seattle: '80',
    'New York': '20',
    Bogota: '20',
    Cali: '40',
    Paris: '2'
};

for (const [data, value] of Object.entries(datas)) {
    client.hset('HolbertonSchools', data, value, (err, reply) => {
        console.log(`Reply: ${reply}`);
    });
};

client.hgetall('HolbertonSchools', function(err, object) {
    console.log(object);
});
