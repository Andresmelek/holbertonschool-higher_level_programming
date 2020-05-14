#!/usr/bin/node

$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json'
  }).done(data => {
    const films = data.results;
    films.forEach(index => {
      $('#list_movies').append(`<li>${index.title}</li>`);
    });
  });
});
