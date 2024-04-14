export default function signUpUser(firstName, lastName) {
  return new Promise((resolve, reject) => {
    // Create an object with the given first and last name
    const user = {
      firstName,
      lastName
    };
    // Resolve the promise with the created object
    resolve(user);
  });
}
