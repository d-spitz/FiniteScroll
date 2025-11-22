function shuffleCards() {
  const container = document.querySelector('.scroll-container');
  const cards = Array.from(container.querySelectorAll('.card'));
  const endMessage = container.querySelector('.end-message');

  // Fisher-Yates shuffle
  for (let i = cards.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [cards[i], cards[j]] = [cards[j], cards[i]];
  }

  // Reappend in shuffled order
  cards.forEach(card => container.appendChild(card));
  container.appendChild(endMessage);
}

document.addEventListener("DOMContentLoaded", () => {
  shuffleCards();
});
