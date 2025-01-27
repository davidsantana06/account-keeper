export const activateNotificationFadeOut = () => {
  const notifications = document.querySelectorAll(".notification");

  notifications.forEach((notification) => {
    setTimeout(() => {
      notification.classList.remove("animate__fadeInRight");
      notification.classList.add("animate__fadeOutRight");
    }, 3 * 1000);
  });
};
