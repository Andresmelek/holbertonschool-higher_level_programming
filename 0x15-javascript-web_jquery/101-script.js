#!/usr/bin/node

document.addEventListener('DOMContentLoaded', event => {
  event.preventDefault();
  $('#add_item').click(function () {
    $('.my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(function () {
    $('ul li').eq(1).remove();
  });
  $('#clear_list').click(function () {
    $('.my_list').empty();
  });
});
