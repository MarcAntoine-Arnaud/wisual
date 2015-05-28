
$("#startJob").submit(function( event ){

	data = { "videos": []}

	data["reference"] = $(this).find( "input[name='reference']" ).val();
	for( var i = 0; i < 5; ++i ){
		var elem = "input[name='video" + i + "']";
		var video = $(this).find( elem ).val();
		if( video == ""){break;}
		data.videos.push(video);
	}
	data["mode"] = $(this).find( "input[name='analysisMode']:checked" ).val();
	console.log(data);
	$.ajax({
		type: "POST",
		data: JSON.stringify(data),
		url: "/job",
		contentType: 'application/json; charset=utf-8'
	})
	.done(function(data){
		console.log(data);
		$(this).notifyMe(
			'bottom',
			'info',
			'Analysis started',
			'New analysis just started now.',
			1000,
			2000
		);
	})
	.error(function(data){
		console.log("error");
	})

	event.preventDefault();
});