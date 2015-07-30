$("#homes").click(function(){
	$("html, body").animate({ scrollTop: 0 }, 500);
});

$("#quensomos").click(function(){
	$("html, body").animate({ scrollTop: $('#quemSomos').offset().top - (1000 + "px")}, 600+"px");
});

$("#events").click(function(){
	$("html, body").animate({ scrollTop: $('#estrutura').offset().top -100 }, 700);
});

$("#servicess").click(function(){
	$("html, body").animate({ scrollTop: $('#local').offset().top -100 }, 700);
});

// Pagina do curso:
$("#contat").click(function(){
	$("html, body").animate({ scrollTop: $('#contato').offset().top -100}, 800);
});