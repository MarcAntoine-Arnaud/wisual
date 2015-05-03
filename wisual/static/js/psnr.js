
$(function() {

$(".inputFile").keyup(function() {
	var datalistId = $(this).attr("list");
	var basepath = $(this).val();
	$.ajax(
		url="/ls" + $(this).val()
	).done(function(data){
		$("#" + datalistId).html("");
		$.each(data.files, function(index, value){
			if( basepath[basepath.length-1] == "/" ){
				$("#" + datalistId).append("<option>" + basepath + value + "</option>");
			}else{
				$("#" + datalistId).append("<option>" + basepath + "/" + value + "</option>");
			}
		});
		$.each(data.directories, function(index, value){
			if( basepath[basepath.length-1] == "/" ){
				$("#" + datalistId).append("<option>" + basepath + value + "/</option>");
			}else{
				$("#" + datalistId).append("<option>" + basepath + "/" + value + "/</option>");
			}
		});
	}).error();
});

});
