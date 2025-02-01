/**
 * Adds a fade-out animation to all notifications after a 3-second delay.
 * The `animate__fadeInRight` class is removed, and the
 * `animate__fadeOutRight` class is added. Executes for all elements with
 * the `notification` class.
 *
 * @returns {void}
 */
export const activateNotificationFadeOut = () => {
  const notifications = document.querySelectorAll(".notification");

  notifications.forEach((notification) => {
    setTimeout(() => {
      notification.classList.remove("animate__fadeInRight");
      notification.classList.add("animate__fadeOutRight");
    }, 3 * 1000);
  });
};
