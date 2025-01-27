import {
  activateCurrentNavbarItem,
  turnOnNavbarMenuToggle,
} from "./_navbar.js";
import { activateNotificationFadeOut } from "./_notification.js";

document.addEventListener("DOMContentLoaded", () => {
  // navbar _
  activateCurrentNavbarItem();
  turnOnNavbarMenuToggle();

  // notification _
  activateNotificationFadeOut();
});
