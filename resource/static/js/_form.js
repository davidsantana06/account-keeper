import { submitRequest } from "./_asyncRequest.js";

/**
 * Applies the `IMask` to all `input` and `textarea` fields with the
 * `data-pattern` attribute. The pattern defined in the `data-pattern`
 * is used to apply the corresponding mask to the field.
 *
 * @returns {void}
 */
export const activateIMask = () => {
  const fields = document.querySelectorAll(
    "input[data-pattern], textarea[data-pattern]"
  );

  fields.forEach((field) => {
    const { pattern } = field.dataset;
    IMask(field, { mask: pattern });
  });
};

/**
 * Enables or disables the submit button based on changes to form fields.
 * The submit button is enabled if any form field is modified. Executes
 * when there is a submit button in the form and monitors `input`, `select`,
 * and `textarea` elements.
 *
 * @returns {void}
 */
export const turnOnDirtyFormCheck = () => {
  const submitField = document.querySelector("input[type='submit']");
  if (!submitField) return;

  const fields = Array.from(
    document.querySelectorAll("input, select, textarea")
  );
  const initialValues = fields.map((field) => field.value);

  fields.forEach((field) => {
    field.addEventListener("input", () => {
      const hasModification = fields.some(
        (curField, curIndex) => curField.value !== initialValues[curIndex]
      );

      if (hasModification) submitField.removeAttribute("disabled");
      else submitField.setAttribute("disabled", "true");
    });
  });
};

/**
 * Attaches an event listener to the form with the `data-action`
 * attribute to handle form submission asynchronously. It prevents the
 * default form submission and sends the form data via an asynchronous
 * request.
 *
 * @returns {void}
 */
export const turnOnFormAsyncRequest = () => {
  const form = document.querySelector("form[data-action]");
  if (!form) return;

  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const { action, method } = form.dataset;
    const body = new FormData(form);

    submitRequest(action, { method, body });
  });
};

/**
 * Toggles the visibility of the password field when the mouse is hovered
 * over it. The password is shown as text on hover and hidden when the
 * mouse leaves the field. Executes for password input fields.
 *
 * @returns {void}
 */
export const turnOnPasswordVisibilityToggle = () => {
  const password = document.querySelector("input[type='password']");
  if (!password) return;

  password.addEventListener("mouseover", () => (password.type = "text"));
  password.addEventListener("mouseout", () => (password.type = "password"));
};
