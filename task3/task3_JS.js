var product1 = {
  id: 355216933,
  quantity: 3
}

var product2 = {
  id: 355216938,
  quantity: 3
}
console.log("Добавлен продукт с ID " + product1.id + " в количестве " + product1.quantity)
console.log("Добавлен продукт с ID " + product2.id + " в количестве " + product2.quantity)

Ecwid.Cart.addProduct(product1);
Ecwid.Cart.addProduct(product2);


Ecwid.Cart.get(function(cart){
  console.log("В корзине продукт с ID " + cart.items[0].product.id + " В количестве: " + cart.items[0].quantity) 
  console.log("В корзине продукт с ID " + cart.items[1].product.id + " В количестве: " + cart.items[1].quantity) 
 if(cart.items[0].product.id == product1.id && cart.items[1].product.id == product2.id){
  	alert("Добавленные позиции находится в корзине, в количестве " + cart.productsQuantity + " штук")
 }else{
   alert("Добавленные позиции НЕ попали в корзину.")
 }
});