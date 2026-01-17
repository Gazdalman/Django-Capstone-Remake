import Cookies from "js-cookie";

export const csrfFetch = async (url, options = {}) => {
  // Set options.method as 'GET' by default
  options.method = options.method || 'GET';
  // Set options.headers to empty obj by default
  options.headers = options.headers || {};

  // If the options.method is not 'GET', then set the "Content-Type" header to
  // "application/json", and set the "X-CSRFToken" header to the value of the
  // "csrftoken" cookie
  if (options.method.toUpperCase() !== 'GET') {
    // CHANGE 1: Only set JSON content type if it's NOT a file upload (FormData)
    // If you force JSON on a file upload, Django won't be able to read the image.
    if (!options.headers['Content-Type'] && !(options.body instanceof FormData)) {
      options.headers['Content-Type'] = 'application/json';
    }

    // CHANGE 2: Django uses 'X-CSRFToken', not 'XSRF-Token'
    // CHANGE 3: Django cookie is named 'csrftoken' by default
    options.headers['X-CSRFToken'] = Cookies.get('csrftoken');
  }

  // Call the default window's fetch with the url and the options passed in
  const res = await window.fetch(url, options);

  // CHANGE 4: I removed the "throw res" block.
  // Your thunks check "if (res.ok)" manually. If we throw here,
  // your thunks will crash unless you wrap them all in try/catch.

  return res;
};

// Call this to get the "csrftoken" cookie, should only be used in development
export const restoreCSRF = () => {
  return csrfFetch('/api/csrf/restore/');
};
