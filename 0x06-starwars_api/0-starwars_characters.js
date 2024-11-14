#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

// Check if a movie ID was provided as an argument
if (process.argv.length > 2) {
  // Fetch the movie data for the given movie ID
  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.error(err);
      return;
    }

    // Parse the response body to extract character URLs
    const charactersURL = JSON.parse(body).characters;

    // Map character URLs to Promises that resolve with character names
    const characterNames = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (error, __, charBody) => {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(charBody).name);
          }
        });
      })
    );

    // Wait for all character names to be fetched and then print them in order
    Promise.all(characterNames)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.error(allErr));
  });
} else {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
}
