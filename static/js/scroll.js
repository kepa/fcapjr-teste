$("#homes").click(function(){
	$("html, body").animate({ scrollTop: 0 }, 500);
});

$("#quensomos").click(function(){
	$("html, body").animate({ scrollTop: $('#quemSomos').offset().top -90 }, 700);
});

$("#equipe").click(function(){
	$("html, body").animate({ scrollTop: $('#team').offset().top -60 }, 700);
});

$("#events").click(function(){
	$("html, body").animate({ scrollTop: $('#evento').offset().top -60 }, 700);
});

$("#servicess").click(function(){
	$("html, body").animate({ scrollTop: $('#servi').offset().top -100 }, 700);
});

// Pagina do curso:
$("#contat").click(function(){
	$("html, body").animate({ scrollTop: $('#contato').offset().top -100 }, 500);
});