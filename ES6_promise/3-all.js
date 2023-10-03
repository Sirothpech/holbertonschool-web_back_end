import { uploadPhoto, createUser } from './utils.js';

function handleProfileSignup() {
  const promises = [uploadPhoto(), createUser()];

  return Promise.all(promises)
    .then((results) => {
        console.log(`${results[0].body} ${results[1].firstName} ${results[1].lastName}`);
      })
    .catch(() => {
      console.log('Signup system offline');
    });
}

export default handleProfileSignup;
