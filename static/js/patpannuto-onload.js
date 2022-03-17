/* vim: set ts=2 sts=2 sw=2 noet: */

$(".pub_bibtex").click(function() {
	var a_id = $(this).attr("id");
	var div_id = a_id.replace('XXXatag_', '');
	$('#'+div_id).toggle();
});

$(".pub_abstract").click(function() {
	var a_id = $(this).attr("id");
	var div_id = a_id.replace('XXXatag_', '');
	$('#'+div_id).toggle();
});

$(".pub_abstract_raw").click(function() {
	var a_id = $(this).attr("id");
	var raw_div_id = a_id.slice(0, -2);
	var html_div_id = a_id.slice(0, -5) + "html";
	$('#'+raw_div_id).hide("slow");
	$('#'+html_div_id).show("slow");
});

$(".pub_abstract_html").click(function() {
	var a_id = $(this).attr("id");
	var html_div_id = a_id.slice(0, -2);
	var raw_div_id = a_id.slice(0, -6) + "raw";
	$('#'+html_div_id).hide("slow");
	$('#'+raw_div_id).show("slow");
});

function pub_type () {
	console.log($(this));
	var chk_val = $(this).attr("value");
	if (this.checked) {
		$('.pub_type_'+chk_val).show("slow");
	} else {
		$('.pub_type_'+chk_val).hide("slow");
	}
}

$(".type_chk").change(pub_type);
$(".type_chk").each(pub_type);

$('.pub_prepub').each(function() {
	var id = $(this).attr("id");
	var temp = id.split("XXX");
	var root = temp[0];
	var pub_date = Date.parse(temp[1]);
	var now = new Date();

	if (pub_date > now) {
		var showhide = function() {
			$('#'+id.replace( /(:|\.|\[|\])/g, "\\$1" )).toggle();
		};

		var title = $('#' + root.replace("-prepub", "-title"));
		var link = $('#' + root.replace("-prepub", "-link"));
		title.attr('href', '#');
		title.click(showhide);
		link.text('[To Appear]');
		link.attr('href', '#');
		link.click(showhide);
	}
});

