function handleResponseFromAPI(promise) {
  promise
    .then((data) => {
      console.log('Got a response from the API');
      return { status: 200, body: 'success' };
    })
    .catch((error) => {
      console.log('Got an error from the API');
      return new Error('');
    });
}

export default handleResponseFromAPI;
