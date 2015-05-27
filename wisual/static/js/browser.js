
$(function() {

$.ajax("/ls")
.done( function(data){
	$("#root").append( "<ul>" );
	$.each( data.directories, function(index, directory){
		$("#root ul").append( '<li><span class="browser-folder"><i class="fa fa-folder-o"></i>' + directory + '</span></li>')
	});
	$.each( data.files, function(index, file){
		$("#root ul").append( '<li><span class="browser-file"><i class="fa fa-file-o"></i>' + file + '</span></li>')
	})
	$("#root").append( "</ul>" );
	$( ".browser-file" ).draggable({ /*revert: "valid", */helper: "clone" });
})
.error( function(){
	console.log("Error during listing on server.");
});

$( ".inputFile" ).droppable({
	drop: function( event, ui ) {
		console.log(ui.draggable.context.innerText);
		$( this ).val( ui.draggable.context.innerText );
	}
});

});