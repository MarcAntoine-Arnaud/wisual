
$("#downloadChart").submit(function( event ){
	format = $(this).find( "input[name='format']:checked" ).val();
	var canvas = document.getElementById("graphResult"); //.getContext("2d");
	var ctx = canvas.getContext("2d");
	event.preventDefault();
	
	switch(format){
		case "png":{
			canvas.toBlob(function(blob) {
			    saveAs(blob, "chart.png");
			}, "image/png");
			break;
		}
		case "jpeg":{
			canvas.toBlob(function(blob) {
			    saveAs(blob, "chart.jpg");
			}, "image/jpeg");
			break;
		}
		default:{
			console.log("unknown format");
			break;
		}
	}
	$("#downloadChart").modal("hide");
});
