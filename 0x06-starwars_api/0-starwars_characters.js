#!/usr/bin/node
/**
 * Retrieves and prints the names of characters from a Star Wars movie.
 */
const request = require('request');

// Validate and retrieve the movie ID from command-line arguments
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Construct the URL for the Star Wars API
const url = `https://swapi.dev/api/films/${movieId}/`;

// Request movie data from the API
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to retrieve data:', response.statusCode);
    return;
  }

  // Parse the movie data
  const movie = JSON.parse(body);
  const characters = movie.characters;

  // Fetch and print character names in order
  const fetchCharacterNames = (characterUrls, index = 0) => {
    if (index === characterUrls.length) {
      return;
    }

    request(characterUrls[index], (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error('Failed to retrieve character data:', response.statusCode);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
      fetchCharacterNames(characterUrls, index + 1);
    });
  };

  fetchCharacterNames(characters);
});
