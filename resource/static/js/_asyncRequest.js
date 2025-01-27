export const submitRequest = async (url, options) => {
  fetch(url, options)
    .then((response) => response.json())
    .then(({ redirect }) => (window.location.href = redirect));
};
