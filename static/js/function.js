function searchToggle(obj, evt){
	var container = $(obj).closest('.search-wrapper');

	if(!container.hasClass('active')){
		container.addClass('active');
		evt.preventDefault();
	}
	else if(container.hasClass('active') && $(obj).closest('.input-holder').length == 0){
		container.removeClass('active');
		// clear input
		container.find('.search-input').val('');
		// clear and hide result container when we press close
		container.find('.result-container').fadeOut(100, function(){$(this).empty();});
	}
}




function submitFn(obj, evt){
	value = $(obj).find('.search-input').val().trim();

	if(!value.length){
		_html = "关键词不能为空。";
		$(obj).find('.result-container').html('<span>' + _html + '</span>');
		$(obj).find('.result-container').fadeIn(100);
	}
	else{

		$.ajax({
			type: 'GET',
			url: /searching/,
			data: {'title':value},
			dataType: 'json',
			success: function(data){
				show_result(data.result);
			},
			error: function(xhr, type){

			}
		})

		evt.preventDefault();
	}

}


function show_result(news) {
	var buffer = '';
	for (var i in news) {
		console.log(news[i][1]);
		buffer += "\
		<a href=" + news[i][1] + " target=\"_blank\">" + news[i][0] + "</a>\
		"
	}
	$("div[class='searchcontainer']").html(buffer);
}
