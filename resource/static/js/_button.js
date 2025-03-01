import { submitRequest } from "./_asyncRequest.js";

/**
 * Attaches click event listeners to all buttons with the `data-action`
 * attribute. When a button is clicked, it triggers an asynchronous
 * request using the `action` and `method` from the button's dataset.
 *
 * @returns {void}
 */
export const turnOnButtonAsyncRequest = () => {
  const buttons = document.querySelectorAll("button[data-action]");

  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      const { action, method } = button.dataset;
      submitRequest(action, { method });
    });
  });
};
