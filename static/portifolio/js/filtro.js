function filtrar(id){

	if(id === 'iventos'){
		$('.iventos').show("slow");
		$('.acon').hide("slow");
		$('.serbico').hide("slow");	
	}

	else if(id === 'serbico'){
		$('.serbico').show("slow");
		$('.acon').hide("slow");
		$('.iventos').hide("slow");	
	}

	else if(id === 'acon'){
		$('.acon').show();
		$('.iventos').hide("slow");
		$('.serbico').hide("slow");	
	}
	else{
		$('.acon').show("slow");
		$('.iventos').show("slow");
		$('.serbico').show("slow");
	}
	
}