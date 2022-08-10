'use strict';

// select elements
const player0El = document.querySelector('.player--0');
const player1El = document.querySelector('.player--1');
const score0El = document.querySelector('#score--0');
const score1El = document.querySelector('#score--1');
const current0El = document.querySelector('#current--0');
const current1El = document.querySelector('#current--1');
const diceEl = document.querySelector('.dice');

const btnNew = document.querySelector('.btn--new');
const btnRoll = document.querySelector('.btn--roll');
const btnHold = document.querySelector('.btn--hold');

// testing
// console.log(player0El);
// console.log(player1El);
// console.log(score0El);
// console.log(score1El);
// console.log(current0El);
// console.log(current1El);

// declare global variables
let score, currentScore, activePlayer, playing;

function init() {
  // reset variables
  score = [0, 0];
  currentScore = 0;
  activePlayer = 0;
  playing = true;

  // resetting UI elements
  score0El.textContent = 0;
  score1El.textContent = 0;
  current0El.textContent = 0;
  current1El.textContent = 0;
  diceEl.classList.add('hidden');
  player0El.classList.add('player--active');
  player1El.classList.remove('player--active');
  player0El.classList.remove('player--winner');
  player1El.classList.remove('player--winner');
}

btnRoll.addEventListener('click', function () {
  if (playing) {
    if (player0El) {
      const diceNum = Math.trunc(Math.random() * 6 + 1);
      console.log(diceNum);
      diceEl.src = `dice-${diceNum}.png`;
      diceEl.classList.remove('hidden');
      if (diceNum != 1) {
        currentScore += diceNum;
        document.querySelector(`#current--${activePlayer}`).textContent =
          currentScore;
      } else switchPlayer();
    }
  }
});

function switchPlayer() {
  // alter current player
  // if current player is 0 make it 1 and vice versa
  // reset current score var
  // reset current score elem of active player
  // toggle current player style
  currentScore = 0;
  document.querySelector(`#current--${activePlayer}`).textContent = 0;
  activePlayer = activePlayer === 0 ? 1 : 0;
  player0El.classList.toggle('player--active');
  player1El.classList.toggle('player--active');
}

btnHold.addEventListener('click', function () {
  // saving current score

  if (playing) {
    score[`${activePlayer}`] += currentScore; // saving current scroe in overall score of the active player
    document.querySelector(`#score--${activePlayer}`).textContent =
      score[`${activePlayer}`]; // display the help scroe on screem
    if (score[`${activePlayer}`] >= 100) {
      playing = false;
      diceEl.classList.add('hidden');
      document
        .querySelector(`.player--${activePlayer}`)
        .classList.remove('player--active');
      document
        .querySelector(`.player--${activePlayer}`)
        .classList.add('player--winner');
    } else switchPlayer();
  }
});

init();
btnNew.addEventListener('click', init);

// function toggleStyle() {
//   player0El.classList.toggle('player--active');
// }
