const $my_list = $('header');
const $divupdate = $('DIV#update_header');
const $txt = $("<li></li>").text("Item");

$divupdate.on('click', () => {
  $my_list.text('New Header!!!')
});
