// Select the element with the ID red_header
const redHeaderTrigger = document.querySelector('#red_header');

// Add a click event listener to that element
redHeaderTrigger.addEventListener('click', function () {
  // Select the header element
  const header = document.querySelector('header');
  // Update its text color to red
  header.style.color = '#FF0000';
});
