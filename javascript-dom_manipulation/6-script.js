// Define the URL for the Star Wars API
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// Use the Fetch API to get the data
fetch(url)
  .then(function (response) {
    // Convert the response to JSON format
    return response.json();
  })
  .then(function (data) {
    // Select the element with ID 'character'
    const characterElement = document.querySelector('#character');
    // Update the text content with the character's name
    characterElement.textContent = data.name;
  })
  .catch(function (error) {
    // Log any errors to the console (good practice)
    console.error('Error fetching data:', error);
  });
