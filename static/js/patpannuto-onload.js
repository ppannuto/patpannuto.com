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
