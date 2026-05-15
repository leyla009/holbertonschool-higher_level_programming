// Define the URL for the Star Wars films API
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

// Fetch the data from the API
fetch(url)
  .then(function (response) {
    // Convert the response to JSON
    return response.json();
  })
  .then(function (data) {
    // Select the ul element where movies will be listed
    const listElement = document.querySelector('#list_movies');
    
    // The films are contained in an array called 'results'
    const movies = data.results;

    // Loop through each movie in the results array
    movies.forEach(function (movie) {
      // Create a new li element
      const listItem = document.createElement('li');
      // Set the text of the li to the movie title
      listItem.textContent = movie.title;
      // Append the li to the ul element
      listElement.appendChild(listItem);
    });
  })
  .catch(function (error) {
    // Handle potential errors
    console.error('Error fetching movies:', error);
  });
