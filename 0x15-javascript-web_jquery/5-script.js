const $my_list = $('ul.my_list');
const $divadditem = $('DIV#add_item');
const $txt = $("<li></li>").text("Item");

$divadditem.on('click', () => {
  $my_list.append('<li>Item</li>')
});
