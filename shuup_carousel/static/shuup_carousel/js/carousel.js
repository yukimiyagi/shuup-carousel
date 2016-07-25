// Set up owl carousel
$(".owl-carousel.one").each(function() {
    var arrowsVisible = JSON.parse($(this).data("arrows-visible").toLowerCase());
    $(this).owlCarousel({
        nav: arrowsVisible,
        navText: [
            '<i class="fa fa-angle-left .carousel-control .icon-prev"></i>',
            '<i class="fa fa-angle-right .carousel-control .icon-prev"></i>'
        ],
        pagination: true,
        items: 1,
    });
});