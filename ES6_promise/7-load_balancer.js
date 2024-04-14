// This script returns the value returned by the promise that resolved the first one.
export default function loadBalancer(chinaDownload, USDownload) {
  return Promise.race([chinaDownload, USDownload]);
}
