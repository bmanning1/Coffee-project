$(document).ready(function () {

    $('.backforum-btn').mouseenter(function () {
        $('.box').css('display', 'block');
        $('.box').css('position', 'fixed');
        $('.box').css('z-index', '1000')
    });
    $('.backforum-btn').mouseleave(function () {
        $('.box').css('display', 'none')
    });
});
