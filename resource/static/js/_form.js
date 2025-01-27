import { submitRequest } from "./_asyncRequest.js";

export const activateIMask = () => {
  const fields = document.querySelectorAll(
    "input[data-pattern], textarea[data-pattern]"
  );

  fields.forEach((field) => {
    const { pattern } = field.dataset;

    const isRegex = pattern.startsWith("r");
    const mask = isRegex ? new RegExp(pattern.slice(1)) : pattern;

    IMask(field, { mask });
  });
};

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

export const turnOnFormAsyncRequest = () => {
  const form = document.querySelector("form[data-action]");
  if (!form) return;

  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const { action, method } = form.dataset;
    const body = new FormData(form);

    await submitRequest(action, { method, body });
  });
};

export const turnOnPasswordVisibilityToggle = () => {
  const password = document.querySelector("input[type='password']");
  if (!password) return;

  password.addEventListener("mouseover", () => (password.type = "text"));
  password.addEventListener("mouseout", () => (password.type = "password"));
};
