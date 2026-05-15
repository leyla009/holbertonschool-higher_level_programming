// Ensure the DOM is fully loaded before running the script
document.addEventListener('DOMContentLoaded', function () {
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';

  // Fetch the translation from the API
  fetch(url)
    .then(function (response) {
      // Convert response to JSON
      return response.json();
    })
    .then(function (data) {
      // Select the element with ID 'hello'
      const helloElement = document.querySelector('#hello');
      // Update its text content with the 'hello' value from the API
      helloElement.textContent = data.hello;
    })
    .catch(function (error) {
      console.error('Error fetching the translation:', error);
    });
});
