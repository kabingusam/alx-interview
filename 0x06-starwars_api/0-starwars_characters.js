#!/usr/bin/node

const request = require('request');
const options = {
    url: 'https://swapi.dev/api/films/3',
    method: 'GET',
    json: true
};

request(options, function (error, response, body) {
    if (!error && response.statusCode == 200) {
        var characters = body.characters;
        characters.forEach(function (character) {
            var characterOptions = {
                url: character,
                method: 'GET',
                json: true
            };
            request(characterOptions, function (error, response, body) {
                if (!error && response.statusCode == 200) {
                    console.log(body.name);
                } else {
                    console.error(error)
                }
            });
        });
    } else {
        console.error(error)
    }
});
