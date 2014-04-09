/**
 * @author Lyd.
 */

$(function(){	
//Ajax for throw the bottle
	$('#paper-form').ajaxForm({
		dataType:'json',
		success: function(response){
			if (response.success) {
				$S.notice(response.message.join('，'),2000);
				setTimeout(function(){
					$('#cancelbtn').click();
				}, 2000);
			}else{
				$S.alert(response.message.join('，'),2000);
			}
		},
		error: function() {
			$S.error('发生技术问题，导致你的提交失败。请联系管理员！');
		}
	});
	
//animate for the forms	
	$('#bottle').hide();
	$('#myBottles').hide();
	$('#infor').html('您还可以写' + (365 - $("#paper").val().length) + '个字');
	$('#throwBtn').click(function(){
		$('#throw-bottles').delay(100).animate({opacity:'0'},200).slideUp(1);
		$('#pick-bottles').delay(100).animate({opacity:'0'},200).slideUp(1);
		$('#myBtn').delay(100).animate({opacity:'0'},200).slideUp(1);
		$('#bottles-bg').delay(400).animate({opacity:'0'}).slideUp();
		$('#bottle').animate({opacity:'100'},1).delay(900).slideDown('slow');
	});
	
	$('#cancelbtn').click(function(){
		$('#bottle').delay(100).animate({opacity:'0'}).delay(200).slideUp();
		$('#bottles-bg').delay(300).slideDown().animate({opacity:'100'});
		$('#myBtn').delay(300).slideDown().animate({opacity:'100'});
		$('#throw-bottles').slideDown(1).delay(500).animate({opacity:'100'},200);
		$('#pick-bottles').slideDown(1).delay(500).animate({opacity:'100'},200);
		
	});
	
	$("#myB-cbtn").click(function(){
		$('#myBottles').delay(100).animate({opacity:'0'}).delay(200).slideUp();
		$('#bottles-bg').delay(300).slideDown().animate({opacity:'100'});
		$('#myBtn').delay(300).slideDown().animate({opacity:'100'});
		$('#throw-bottles').slideDown(1).delay(500).animate({opacity:'100'},200);
		$('#pick-bottles').slideDown(1).delay(500).animate({opacity:'100'},200);
	});
	
	$('#myBtn').click(function(){
		$('#throw-bottles').delay(100).animate({opacity:'0'},200).slideUp(1);
		$('#pick-bottles').delay(100).animate({opacity:'0'},200).slideUp(1);
		$('#myBtn').delay(100).animate({opacity:'0'},200).slideUp(1);
		$('#bottles-bg').delay(400).animate({opacity:'0'}).slideUp();
		$('#myBottles').animate({opacity:'100'},1).delay(900).slideDown('slow');
		Drift.myBottles();
	});
	
	$('#paper').keyup(function(){
		
		if($("#paper").val().length <= 0 || $("#paper").val().length <= 365 ){ 
			$('#throwsubmit').removeClass('disabled');
			$('#throwsubmit').attr('disabled','')
		}else{
			$('#throwsubmit').addClass('disabled');
			$('#throwsubmit').attr('disabled','disabled');
		}
		
		if($("#paper").val().length >= 365){
			$('#infor').html('<font color="8a0000">已经超出' + ( $("#paper").val().length - 365 ) + '个字</font>');
		}else{
			$('#infor').html('您还可以写' +( 365- $("#paper").val().length) + '个字');
		}
	});

	
	
});
