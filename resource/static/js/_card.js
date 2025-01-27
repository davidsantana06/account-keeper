export const turnOnCardRedirect = () => {
  const cards = document.querySelectorAll(".card[data-href]");

  cards.forEach((card) => {
    card.addEventListener("click", () => {
      const { href } = card.dataset;
      window.location.href = href;
    });
  });
};
