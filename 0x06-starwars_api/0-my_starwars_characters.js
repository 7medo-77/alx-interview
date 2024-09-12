#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

async function enumerateCharactersByOrder (arrayOfLinks) {
  for (const link of arrayOfLinks) {
    const name = await fetch(link)
      .then(result => result.json())
      .then(jsonRes => jsonRes.name);
    console.log(name);
  }
}

// let charArray;

request(url, (error, response, body) => {
  if (!error) {
    const result = JSON.parse(body);
    const charArray = result.characters;
    enumerateCharactersByOrder(charArray);
  } else {
    console.error('Error:', error);
  }
});
