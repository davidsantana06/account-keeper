import { turnOnCardRedirect } from "./_card.js";
import {
  activateCurrentNavbarItem,
  turnOnNavbarMenuToggle,
} from "./_navbar.js";

document.addEventListener("DOMContentLoaded", () => {
  // navbar _
  activateCurrentNavbarItem();
  turnOnNavbarMenuToggle();

  // card _
  turnOnCardRedirect();
});
