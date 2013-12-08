(function(window, $) {	
	var szuneedyou = {};
	var baseurl = '/';		//与application/bootstrap.php  baseurl保持一致
	
	
	
	// 初始化全站统一元素
	szuneedyou.elementInit = function() {
		$('body').prepend($('<div id="message-box"></div>')); // 信息框容器
		$('body').prepend($('<div id="login-box"></div>')); // 登录框
	};
	
	// 全站统一信息提示框
	szuneedyou._messagebox = function(message, timeout, specialClass) {
		var entity = $('<div class="message-content"></div>')
			.hide()
			.append($('<span class="message-text"></span>').append(message))
			.append($('<a href="javascript:void(0);" class="button message-close-btn">关闭</a>'))
			.addClass(specialClass);
		
		$('#message-box').append(entity);
		
		entity.fadeIn(500);
		
		if (timeout > 0) {
			setTimeout(function(){
				entity.fadeOut(500, function(){
					$(this).remove();
				});
			}, timeout);
		}
		
		entity.children('a.message-close-btn').click(function(){
			entity.fadeOut(500, function(){
				$(this).remove();
			});
		});
	};
		
	szuneedyou.notice = function(message, timeout) { this._messagebox(message, timeout, 'notice'); };
	szuneedyou.alert  = function(message, timeout) { this._messagebox(message, timeout, 'alert');  };
	szuneedyou.error  = function(message, timeout) { this._messagebox(message, timeout, 'error'); };
	
	szuneedyou.redirct = function(url){ document.location= baseurl + url ;};
	
	szuneedyou.webroot = baseurl;
	szuneedyou.baseroot = baseurl;
	
	/*
	 *  与 application/
	 */
		
	window.szuneedyou = window.$S = szuneedyou;
})(window, jQuery);

$(function(){
	// 初始化元素
	$S.elementInit();
});
