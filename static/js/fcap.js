var buttonConstName = 'area';
var buttonId = 1;

var curClass = 'image-1';
var button = document.getElementById(buttonConstName + buttonId);

var equipeSection = document.getElementById('equipeSection');

var title = document.getElementById('title');
var description = document.getElementById('description');

var tempTitles = ['posição queimada', 'area 1', 'area 2', 'area 3', 'area 4', 'area 5']
var tempDescriptions = ['posição queimada', 'area 1 é a area mais massa de boa', 'area 2 nao fica pra tras da area 1', 'area 3 é a melhor!!!', 'area 4 top top!', 'area 5 é a mais comum']

while(button){
	button.addEventListener('click', function(){

		equipeSection.classList.remove(curClass)
		
		var curIdNumber = this.id.substring(4, 5);

		curClass = 'image-' + curIdNumber;

		equipeSection.classList.add(curClass);
		title.innerHTML = tempTitles[curIdNumber];
		description.innerHTML = tempDescriptions[curIdNumber];
	});

	buttonId += 1;
	button = document.getElementById(buttonConstName + buttonId);
}