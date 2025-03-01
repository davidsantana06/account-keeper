/**
 * Activates the current navbar item by comparing the URL path with the
 * `href` attribute of each navbar item. If a match (exact or partial)
 * is found, the navbar item gets additional styling classes applied.
 *
 * @returns {void}
 */
export const activateCurrentNavbarItem = () => {
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
 * Toggles the visibility of the navbar menu when the navbar burger is
 * clicked. The corresponding menu is shown or hidden by toggling the
 * `is-active` class.
 *
 * @returns {void}
 */
export const turnOnNavbarMenuToggle = () => {
  const navbarBurgers = document.querySelectorAll(".navbar-burger");

  navbarBurgers.forEach((navbarBurger) => {
    navbarBurger.addEventListener("click", () => {
      const { target } = navbarBurger.dataset;

      navbarBurger.classList.toggle("is-active");
      document.querySelector(target).classList.toggle("is-active");
    });
  });
};
