// Select the element with the ID update_header
const updateHeaderTrigger = document.querySelector('#update_header');

// Add a click event listener to the trigger
updateHeaderTrigger.addEventListener('click', function () {
  // Select the header element
  const header = document.querySelector('header');
  
  // Update the text content of the header
  header.textContent = 'New Header!!!';
});
