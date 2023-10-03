import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

function handleProfileSignup(firstName, lastName, fileName) {
  const promises = [signUpUser(firstName, lastName), uploadPhoto(fileName)];

  return Promise.allSettled(promises).then((results) => {
    return results.map((result) => {
      if (result.status === 'fulfilled') {
        return { status: 200, value: result.value };
      } else {
        return { status: 500, value: result.reason.message };
      }
    });
  });
}

export default handleProfileSignup;
