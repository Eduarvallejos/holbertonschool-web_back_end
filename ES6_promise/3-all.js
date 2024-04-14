// Import functions from utils.js
import { uploadPhoto, createUser } from './utils';

// Define the handleProfileSignup function
export default function handleProfileSignup() {
  // Promise.all is used to wait for the resolution of both promises
  return Promise.all([uploadPhoto(), createUser()])
    .then((results) => {
      // Destructure the results to access the body of each response
      const [photoResult, userResult] = results;
      console.log(`${photoResult.body} ${userResult.firstName} ${userResult.lastName}`);
    })
    // Handle the error in case one of the promises is rejected
    .catch(() => console.log('Signup system offline'));
}
