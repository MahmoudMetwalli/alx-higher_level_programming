const $my_list = $('header');
const $divadditem = $('DIV#update_header');
const $txt = $("<li></li>").text("Item");

$divadditem.on('click', () => {
  $my_list.text('New Header!!!')
});
