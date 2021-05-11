from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get("https://tsars.company.site/products/OBRAZETS-Cherny-top-p355216933")

time.sleep(2)
js2 = """
Ecwid.Cart.addProduct(355216933)
"""
driver.execute_script(js2)

"""<a class="ec-cart-item__title">ОБРАЗЕЦ. Черный топ</a>"""

driver.get("https://tsars.company.site/products/cart")
time.sleep(2)
check_js = """Ecwid.Cart.get(function(cart){
  if(cart.items[0].product.id == 355216933){
  	alert("Добавленная позиция находится в корзине.");
 }
});"""

driver.execute_script(check_js)
