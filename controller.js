window.onload = function () {
	var play = document.createElement('a');
	play.href = '#';
	play.className = 'btn';
	play.textContent = 'Play Game';
	play.onclick = function () {
		Custom();
		return false;
	};
	document.body.appendChild(play);
};
