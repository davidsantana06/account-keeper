import { turnOnCardRedirect } from "./_card.js";
import {
  activateCurrentNavbarItem,
  turnOnNavbarMenuToggle,
} from "./_navbar.js";
import { activateNotificationFadeOut } from "./_notification.js";

document.addEventListener("DOMContentLoaded", () => {
  // navbar _
  activateCurrentNavbarItem();
  turnOnNavbarMenuToggle();

  // card _
  turnOnCardRedirect();

  // notification _
  activateNotificationFadeOut();
});
