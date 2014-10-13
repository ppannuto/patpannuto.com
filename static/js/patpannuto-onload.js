/* vim: set ts=2 sts=2 sw=2 noet: */

if ($('#gallery-pat-div').is(":visible")) {
	var gallery_img_idx = 1;

	function nextImage () {
		gallery_img_idx += 1;
		var newimg = $('<img />').attr('src', '/images/gallery/'+gallery_img_idx+'.jpg').load(function drawNextImage () {
			if (!this.complete || typeof this.naturalWidth == "undefined" || this.naturalWidth == 0) {
				console.log("Error loading image " + gallery_img_idx);
			} else {
				$('#gallery-pat-div > img').fadeTo(1000, 0.0);
				$('#gallery-pat-div').append(newimg);
				$('#gallery-pat-div > img').last().css('opacity', 0).fadeTo(1000, 1.0, function () {
					$('#gallery-pat-div > img').first().remove();
				});
				window.setTimeout(nextImage, 5000);
			}
		});
	}

	var gallery = $("<img />").attr('src', '/images/gallery/'+gallery_img_idx+'.jpg').load(function initGallery () {
		if (!this.complete || typeof this.naturalWidth == "undefined" || this.naturalWidth == 0) {
			console.log("Error loading image gallery");
			$("#gallery-pat-div").hide();
		} else {
			$("#gallery-pat-div").append(gallery);
			window.setTimeout(nextImage, 5000);
		}
	});
}

$(".pub_bibtex").click(function() {
	var a_id = $(this).attr("id");
	var div_id = a_id.replace('XXXatag_', '');
	$('#'+div_id).slideToggle( "slow" );
});

$(".pub_abstract").click(function() {
	var a_id = $(this).attr("id");
	var div_id = a_id.replace('XXXatag_', '');
	$('#'+div_id).slideToggle( "slow" );
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

$(".type_chk").change(function() {
	var chk_val = $(this).attr("value");
	if (this.checked) {
		$('.pub_type_'+chk_val).show("slow");
	} else {
		$('.pub_type_'+chk_val).hide("slow");
	}
});

$('.pub_prepub').each(function() {
	var id = $(this).attr("id");
	var temp = id.split("XXX");
	var root = temp[0];
	var pub_date = Date.parse(temp[1]);
	var now = new Date();

	if (pub_date > now) {
		var showhide = function() {
			$('#'+id.replace( /(:|\.|\[|\])/g, "\\$1" )).slideToggle("slow");
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

