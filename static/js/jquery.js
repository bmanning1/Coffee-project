$(document).ready(function () {

    $('.choices-coffee-info>ul>li>a').click(function () {
        $('.choices-coffee-info>ul>li>a').removeClass('active');
        $('this').addClass('active');
    });

});
