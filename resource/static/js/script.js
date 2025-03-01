import { turnOnCardRedirect } from "./_card.js";
import {
  activateIMask,
  turnOnDirtyFormCheck,
  turnOnFormAsyncRequest,
  turnOnPasswordVisibilityToggle,
} from "./_form.js";
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

  // form _
  activateIMask();
  turnOnPasswordVisibilityToggle();
  turnOnDirtyFormCheck();
  turnOnFormAsyncRequest();

  // notification _
  activateNotificationFadeOut();
});
