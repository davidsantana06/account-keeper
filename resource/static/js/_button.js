import { submitRequest } from "./_asyncRequest.js";

export const turnOnButtonAsyncRequest = () => {
  const buttons = document.querySelectorAll("button[data-action]");

  buttons.forEach((button) => {
    button.addEventListener("click", async () => {
      const { action, method } = button.dataset;
      await submitRequest(action, { method });
    });
  });
};
