import { createClient, print } from 'redis';
import { promisify } from 'util';


const client = createClient();

client.on('connect', () => console.log('Redis client connected to the server'));

client.on('error', (error) => console.log(`Redis client not connected to the server: ${error}`));

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, function(err, reply) {
        print(`Reply: ${reply}`);
    });
}

const get = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
    const result = await get(schoolName);
    console.log(result);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
