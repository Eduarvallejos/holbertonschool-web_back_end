// Define and export the uploadPhoto function
export default function uploadPhoto(filename = String) {
  return new Promise((resolve, reject) => {
    // Reject the promise with an error that includes the file name
    reject(new Error(`${filename} cannot be processed`));
  });
}
