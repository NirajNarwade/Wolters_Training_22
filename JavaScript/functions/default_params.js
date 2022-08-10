const bookings = [];
const bookFlight = function (
  flightNum,
  numPassengers = 1,
  price = 2500 * numPassengers
) {
  const booking = {
    flightNum,
    numPassengers,
    price,
  };

  bookings.push(booking);
};

bookFlight("6E149");
bookFlight("6E149", 2, 5000);
bookFlight("6E149", 3);
bookFlight("6E149", 4);
bookFlight("6E149", undefined, 4000);
console.log(bookings);
