const try_link = $('#try_link');
const landing_header = $('#landing_header');
const landing_content = $('#landing_content');
const about_head = $('#about_head');

make_button_light = name => {
  name
    .removeClass('btn-primary')
    .removeClass('text-light')
    .addClass('btn-light')
    .addClass('text-primary');
};

make_button_primary = name => {
  name
    .removeClass('btn-light')
    .removeClass('text-primary')
    .addClass('btn-primary')
    .addClass('text-light');
};

responsive = () => {
  if ($(window).width() < 567) {
    // Small devices (landscape phones, 576px and up)
    make_button_light(try_link);
    about_head.removeClass('display-4');
    landing_header.removeClass('display-4');
    landing_content.addClass('container');
  } else if ($(window).width() >= 567 && $(window).width() <= 768) {
    // Medium devices (tablets, 768px and up)
    make_button_light(try_link);
    about_head.removeClass('display-4');
    landing_header.removeClass('display-4');
    landing_content.removeClass('container');
  } else if ($(window).width() > 768 && $(window).width() <= 992) {
    // Large devices (desktops, 992px and up)
    make_button_primary(try_link);
    about_head.addClass('display-4');
    landing_header.removeClass('display-4');
    landing_content.addClass('container');
  } else if ($(window).width() > 992 && $(window).width() <= 1200) {
    // Extra large devices (large desktops, 1200px and up)
    make_button_primary(try_link);
    about_head.addClass('display-4');
    landing_header.addClass('display-4');
    landing_content.addClass('container');
  } else {
    make_button_primary(try_link);
    about_head.addClass('display-4');
    landing_header.addClass('display-4');
  }
};

$(window).resize(function() {
  responsive();
});
$(window).ready(function() {
  responsive();
});


// Messages function
setTimeout(function() {
  $('#message').fadeOut('slow')
}, 3000)