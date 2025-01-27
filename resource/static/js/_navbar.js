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
