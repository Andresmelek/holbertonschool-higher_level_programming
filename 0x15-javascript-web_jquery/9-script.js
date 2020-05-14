#!/usr/bin/node

document.addEventListener('DOMContentLoaded', event => {
  event.preventDefault();

  $(function () {
    $.ajax({
      type: 'GET',
      url: 'https://fourtonfish.com/hellosalut/?lang=fr'
    }).done(data => {
      $('#hello').text(data.hello);
    });
  });
});
