(function() {

  $(function() {
    var fadeOut, fade_out;
    fade_out = function(_element) {
      _element.children('div').removeClass('bind-animate');
      _element.children('div').slideUp();
      _element.children('div').addClass('fade-out');
      setTimeout(function() {
        _element.remove();
      }, 500);
    };
    bindAction = function() {
      $("#flash-messages-container > a").click(function() {
        fade_out($(this));
      });
      $(".message-box-fixed").children("a").children("div").each(function() {
        var element_padding, element_width;
        element_padding = $(this).css('padding').split(' ')[1].replace('px', '');
        element_width = $(this).width() + element_padding * 2;
        $(this).css({
          'margin-left': '-' + element_width / 2 + 'px'
        });
        console.log('tse');
      });
    }
    fadeOutAll = function() {
      setTimeout(function() {
        fade_out($("#flash-messages-container > a"));
      }, 2500);
    };
    window.flash_message = function(message, category) {
      var a_html, clear_html;
      if (typeof category === 'undefined') {
        category = 'notice';
      }
      a_html = $('<a href="javascript:void(0)" class="message-box-btn close-btn"></a>').append($('<div class="flash-message-box bind-animate message-box-' + category + '"></div>').append(message));
      clear_html = $('<div style="clear:both;"></div>');
      $("#flash-messages-container").append(a_html);
      $("#flash-messages-container").append(clear_html);
      fadeOutAll();
      bindAction();
    };
    bindAction();
    fadeOutAll();
  });

}).call(this);
