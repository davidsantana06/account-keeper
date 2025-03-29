/**
 * Highlights current navbar item by comparing URL with href attributes.
 * Applies style classes to the matching item (exact or partial match).
 */
const activateCurrentNavbarItem = () => {
  const urlPath = window.location.pathname;
  const navbarItems = document.querySelectorAll(".navbar-item");

  for (const navbarItem of navbarItems) {
    const href = navbarItem.getAttribute("href");

    const isExactMatch = urlPath === href;
    const isPartialMatch = urlPath.startsWith(href) && href !== "/";

    if (!isExactMatch && !isPartialMatch) continue;

    navbarItem.classList.add(
      "button",
      "is-primary",
      "is-inverted",
      "is-hovered",
      "is-radiusless",
      "has-text-left",
      "has-text-centered-desktop"
    );
    break;
  }
};

/**
 * Toggles navbar menu visibility when burger icon is clicked.
 * Adds/removes `is-active` class to show or hide the menu.
 */
const turnOnNavbarMenuToggle = () => {
  const navbarBurgers = document.querySelectorAll(".navbar-burger");

  navbarBurgers.forEach((navbarBurger) => {
    navbarBurger.addEventListener("click", () => {
      const { target } = navbarBurger.dataset;

      navbarBurger.classList.toggle("is-active");
      document.querySelector(target).classList.toggle("is-active");
    });
  });
};

/**
 * Applies IMask to fields with the `data-mask` or `data-regex` attribute.
 */
const activateIMask = () => {
  const fields = document.querySelectorAll(
    "input[data-pattern], textarea[data-pattern]"
  );

  fields.forEach((field) => {
    const { pattern } = field.dataset;
    IMask(field, { mask: pattern });
  });
};

/**
 * Enables/disables submit button based on form field changes.
 * The button activates when any field is modified.
 */
const turnOnDirtyFormCheck = () => {
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
 * Toggles password field visibility on mouse hover.
 * Shows text on hover and hides when mouse leaves.
 */
const turnOnPasswordVisibilityToggle = () => {
  const password = document.querySelector("input[type='password']");
  if (!password) return;

  password.addEventListener("mouseover", () => (password.type = "text"));
  password.addEventListener("mouseout", () => (password.type = "password"));
};

/**
 * Sets up redirects when clicking cards with `data-href`.
 * Navigates to the URL specified in the card's href dataset attribute.
 */
const turnOnCardRedirect = () => {
  const cards = document.querySelectorAll(".card[data-href]");

  cards.forEach((card) => {
    card.addEventListener("click", () => {
      const { href } = card.dataset;
      window.location.href = href;
    });
  });
};

/**
 * Adds fade-out animation to notifications after 3 seconds.
 * Replaces `animate__fadeInRight` with `animate__fadeOutRight` class.
 */
const activateNotificationFadeOut = () => {
  const notifications = document.querySelectorAll(".notification");

  notifications.forEach((notification) => {
    setTimeout(() => {
      notification.classList.remove("animate__fadeInRight");
      notification.classList.add("animate__fadeOutRight");
    }, 3 * 1000);
  });
};

document.addEventListener("DOMContentLoaded", () => {
  // navbar_
  activateCurrentNavbarItem();
  turnOnNavbarMenuToggle();

  // form_
  activateIMask();
  turnOnDirtyFormCheck();
  turnOnPasswordVisibilityToggle();

  // card_
  turnOnCardRedirect();

  // notification_
  activateNotificationFadeOut();
});
