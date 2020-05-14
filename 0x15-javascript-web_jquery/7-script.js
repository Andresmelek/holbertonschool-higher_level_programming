#!/usr/bin/node

$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  }).done(data => {
      $('#character').text(data.name);
    });
});
