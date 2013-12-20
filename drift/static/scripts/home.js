/**
 * @author Lyd.
 */

$(function(){   
//Ajax for reg.
    $('#reg-form').ajaxForm({
        dataType:'json',
        success: function(response){
            if (response.success) {
                $S.notice(response.messages.join('，'),2000);
                setTimeout(function(){
                    $S.redirct('account');
                }, 2000);
            }else{
                $S.alert(response.messages.join('，'),2000);
            }
        },
        error: function() {
            $S.error('发生技术问题，导致你的报名失败。请联系管理员！');
        }
    });
    
//Ajax for login
    $('#login-form').ajaxForm({
        dataType:'json',
        success: function(response){
            if (response.success) {
                $S.notice(response.messages.join('，'),2000);
                setTimeout(function(){
                    $S.redirct('account');
                }, 2000);
            }else{
                $S.alert(response.messages.join('，'),2000);
            }
        },
        error: function() {
            $S.error('发生技术问题，导致你的报名失败。请联系管理员！');
        }
    });
    
//animate for change the forms  
    $('#register').animate({opacity:'0',height:'-=40%',width:'-=40%',left:'+=20%',top:'+=20%'},1);
    $('#register').hide();
    $('.to_register').click(function(){
        $('#login').animate({opacity:'0',width:'-=40%',left:'-=100%'},500);
        $('#register').animate({opacity:'1',height:'+=40%',width:'+=40%',left:'-=20%',top:'-=20%'},500);
    });
    
    $('.to_login').click(function(){
        $('#register').animate({opacity:'0',height:'-=40%',width:'-=40%',left:'+=20%',top:'+=20%'},500);
        $('#login').animate({opacity:'1',width:'+=40%',left:'+=100%'},500);
    });

    
});