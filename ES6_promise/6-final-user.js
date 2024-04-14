// Import the signUpUser and uploadPhoto functions
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

// Define and export the handleProfileSignup function
export default function handleProfileSignup(firstName, lastName, fileName) {
  // Call the signUpUser and uploadPhoto functions
  const promise1 = signUpUser(firstName, lastName);
  const promise2 = uploadPhoto(fileName);

  // Use Promise.allSettled to wait for resolution of both promises
  return Promise.allSettled([promise1, promise2]);
}
