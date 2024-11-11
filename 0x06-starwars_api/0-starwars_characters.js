#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/3/`;

request(url, function (error, response, body) {
  if (error) {
    console.log('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.log('Failed to retrieve data:', response.statusCode);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.log('Error:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.log('Failed to retrieve character data:', response.statusCode);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
