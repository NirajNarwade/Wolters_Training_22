const bookings = [];
const bookFlight = function (flightNum, numPassengers, price) {

  numPassengers ||= 1;
  price ||= 2000;

  const booking = {
    flightNum,
    numPassengers,
    price,
  };

  bookings.push(booking);
};

bookFlight("6E149");
bookFlight("6E149", 4);
bookFlight("6E149", 4, 10000);
console.log(bookings);
