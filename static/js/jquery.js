$(document).ready(function () {

    /* About page Coffee choices Pills */
    $('.choices-coffee-info>ul>li>a').click(function () {
        $('.choices-coffee-info>ul>li>a').removeClass('active');
        $('this').addClass('active');
    });

    /* About page 'Our Aim' */
    $('.About-info>p>span').mouseover(function () {
        $(this).animate({fontSize: '26px'}, 'slow');
    });
    $('.About-info>p>span').mouseout(function () {
        $(this).animate({fontSize: '22px'}, 'slow');
    });

    /* About page animated hover on Member's picture */
    $('img.members').mouseover(function () {
        $(this).animate({borderWidth: '7px'}, 'slow');
        $(this).animate({borderColor: '#bdbdbd'}, 'slow');
    });
    $('img.members').mouseout(function () {
        $(this).animate({borderWidth: '1px'}, 'slow');
        $(this).animate({borderColor: '#4b4b4b'}, 'slow');
    });

    /* Display text to show what the number in the coffee pot on the profile page means when hovered over */
    $('.Coffees-left').mouseover(function () {
        $('.tooltiptext').css({'display': 'inherit'});
    });
    $('.Coffees-left').mouseout(function () {
        $('.tooltiptext').css({'display':'none'});
    });
    $('.tooltiptext').click(function () {
        $('.tooltiptext').css({'display':'none'});
    });

});
