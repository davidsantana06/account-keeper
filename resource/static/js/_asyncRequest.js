/**
 * Sends a fetch request to the specified URL with the provided options.
 * The response will always contain a `redirect` field, and the location
 * will be redirected.
 *
 * @param {string} url - The URL to which the request is sent.
 * @param {object} options - The options for the fetch request (e.g., method, headers).
 * @returns {void}
 */
export const submitRequest = (url, options) => {
  fetch(url, options)
    .then((response) => response.json())
    .then(({ redirect }) => (window.location.href = redirect));
};
