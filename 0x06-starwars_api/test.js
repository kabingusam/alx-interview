#!/usr/bin/node

var request = require('request');

var options = {
    url: 'https://swapi.dev/api/people/2',
    method: 'GET',
    json: true
};

request(options, function (error, response, body) {
    if (!error && response.statusCode == 200) {
        console.log(body.name);
    } else {
        console.error(error);
    }
});
