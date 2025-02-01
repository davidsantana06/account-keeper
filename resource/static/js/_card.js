/**
 * Attaches click event listeners to all elements with the `card` class
 * and the `data-href` attribute. When a card is clicked, the browser
 * navigates to the URL specified in the `href` field of the card's
 * dataset.
 *
 * @returns {void}
 */
export const turnOnCardRedirect = () => {
  const cards = document.querySelectorAll(".card[data-href]");

  cards.forEach((card) => {
    card.addEventListener("click", () => {
      const { href } = card.dataset;
      window.location.href = href;
    });
  });
};
