function show_button() {
	var button = document.getElementsByClassName("updown");
	for (var i=0; i<button.length; i++) {
		if (button[i].style.display == "none") {
			button[i].style.display = "block";	
		} else {
			button[i].style.display = "none";
		}
		
	}
}