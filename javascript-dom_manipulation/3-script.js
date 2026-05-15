// Select the element with the ID toggle_header
const toggleTrigger = document.querySelector('#toggle_header');

// Add a click event listener to the toggle trigger
toggleTrigger.addEventListener('click', function () {
  // Select the header element
  const header = document.querySelector('header');

  // Check if the current class is 'red'
  if (header.classList.contains('red')) {
    // If it's red, remove red and add green
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    // Otherwise (if it's green or anything else), remove green and add red
    header.classList.remove('green');
    header.classList.add('red');
  }
});
