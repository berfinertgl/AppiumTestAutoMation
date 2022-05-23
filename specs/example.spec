Getting Started with Gauge
==========================

This is an executable specification file. This file follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.
To execute this specification, use `mvn test`



Wait
--------------
* "3" kadar bekle

ProductRelatedTransactions
--------
* "2" kadar bekle
* Elementli "//*[@resource-id='com.ozdilek.ozdilekteyim:id/tv_startShoppingStore']" bul ve "ALIŞVERİŞE BAŞLA" değerini kontrol et
* "3" kadar bekle
*"com.ozdilek.ozdilekteyim:id/tv_startShoppingStore" İd'li elemente tıkla
*"3" kadar bekle
* "//*[@resource-id='com.ozdilek.ozdilekteyim:id/nav_categories']" xpath'li elemente tıkla
*"2" kadar bekle
*"//*[@resource-id='com.ozdilek.ozdilekteyim:id/relLayCategoriesItem'][2]" xpath'li elemente tıkla
*"2" kadar bekle
*"//*[@resource-id='com.ozdilek.ozdilekteyim:id/relLayCategoriesItem'][10]" xpath'li elemente tıkla
*"3" kadar bekle
*Sayfayı yukarı kaydır
*"1" kadar bekle
*Sayfayı yukarı kaydır
*"3" kadar bekle
*random ürün seçimi
*"3" kadar bekle
*"//*[@resource-id='com.ozdilek.ozdilekteyim:id/imgFav']" xpath'li elemente tıkla
*"3" kadar bekle
*"com.ozdilek.ozdilekteyim:id/etEposta" id'li elemente "seleniumprojemail@gmail.com" değerini yaz
*"1" kadar bekle
*"com.ozdilek.ozdilekteyim:id/etPassword" id'li elemente "p@$$w0rd..!" değerini yaz
*"2" kadar bekle
*"com.ozdilek.ozdilekteyim:id/btnLogin" İd'li elemente tıkla
*"2" kadar bekle
*"com.ozdilek.ozdilekteyim:id/ivBack" İd'li elemente tıkla
*"com.ozdilek.ozdilekteyim:id/ivBack" İd'li elemente tıkla
*"2" kadar bekle
*random ürün seçimi
*"2" kadar bekle
*random beden seçimi
*"1" kadar bekle
*"com.ozdilek.ozdilekteyim:id/relLayAddCartBtn" İd'li elemente tıkla
*"2" kadar bekle