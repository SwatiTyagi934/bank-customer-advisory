(function (i, s, o, g, r, a, m) {
	i['GoogleAnalyticsObject'] = r;
	i[r] = i[r] || function () {
		(i[r].q = i[r].q || []).push(arguments)
	}, i[r].l = 1 * new Date();
	a = s.createElement(o),
		m = s.getElementsByTagName(o)[0];
	a.async = 1;
	a.src = g;
	m.parentNode.insertBefore(a, m)
})(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga');


//use trigger click to call the parent class

$(document).ready(function (e) {

	$(".tab_in_sec .panel-default>.panel-heading a").click(function () {
		if ($(this).is('.active')) {
			$(this).removeClass("active");
		} else {
			$(".tab_in_sec .panel-default>.panel-heading a.active").removeClass("active");
			$(this).addClass("active");
		}
	});

	$('.aa').on('click', function () {
		$('#headingOne a').trigger('click');
	});

	$('.bb').on('click', function () {
		$('#headingTwo a').trigger('click');
	});

	$('.cc').on('click', function () {
		$('#headingThree a').trigger('click');
	});

	$('#headingOne').on('click', function () {
		$('.aa').addClass('actives').parent('li').siblings('li').find('a').removeClass('actives');
	});

	$('#headingTwo').on('click', function () {
		$('.bb').addClass('actives').parent('li').siblings('li').find('a').removeClass('actives');
	});

	$('#headingThree').on('click', function () {
		$('.cc').addClass('actives').parent('li').siblings('li').find('a').removeClass('actives');
	});


	$('.tab_first .panel-heading ul li a[data-toggle="collapse"]').on('click', function () {
		$('.tab_first .panel-heading ul li a[data-toggle="collapse"]').removeClass('actives');
		$(this).addClass('actives');
	});


	$('.palceholder').click(function () {
		$(this).siblings('input').focus();
	});
	$('.form-control').focus(function () {
		$(this).siblings('.palceholder').hide();
	});
	$('.form-control').blur(function () {
		var $this = $(this);
		if ($this.val().length == 0)
			$(this).siblings('.palceholder').show();
	});
	$('.form-control').blur();


	$('.tab_first .panel-heading ul li a[href^="#"]').on('click', function (event) {
		var target = $(this.getAttribute('href'));

		if (target.length) {
			event.preventDefault();
			$('html, body').stop().animate({
				scrollTop: target.offset().top - 70
			}, 1000);
		}

	});

});