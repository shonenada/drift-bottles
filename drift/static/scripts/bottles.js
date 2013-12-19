$(document).ready(function(){
						   
	$.extend({getRandom:function(x,y){return (parseInt(Math.random() * (y - x + 1) + x))}});
	
	$.extend({setY:function(bottle){bottle.animate({top:$.getRandom(25,450) + "px"},1)}});
	//$.extend({setX:function(bottle){bottle.animate({right:$.getRandom(-31,20) + "px"},1)}});
	$.extend({setX:function(bottle){bottle.animate({right:$.getRandom(-60,-31) + "px"},1)}});
	$.extend({init:function(bottle){$.setX(bottle);$.setY(bottle)}});
	$.extend({float:function(bottles){bottles.animate({top:'-=30px',right:"+=20px"},3000).delay(200).animate({top:'+=30px',right:"+=20px"},3000);}});			   
						   
 	i = 1;
	var stm = function(){ $.ajax({
		url:'/bottles/get/page/'+1 ,
		type:'get',
		async:true ,
		dataType:'json',
		success:function(response){
		$("#bottles").append("<div id='bottle-"+i+"' class='bottle'><div id='bottle-content-" + i + "' class='bottle-content'>"+ response[i-1].content  +"</div><div id='bottle-bottle-"+ i +"' num='"+i+"' class='bottle-bottle'><img src='/static/images/bottle.png' /></div></div>");
			},
		complete:function(){
			$("#bottle-content-"+i).hide();
			$("#bottle-bottle-"+i).click(function(){
   				$(".bottle-content").hide();
				$(".bottle-bottle").find("img").animate({width:"31px",height:"61px"});
				$(this).find('img').animate({width:"+=10px",height:"+=20px"});
				$("#bottle-content-" + $(this).attr('num')).fadeIn('slow');
			});
			$("#bottle-bottle-"+i).each(function(){$.init($(this));});
			$("#bottle-bottle-"+i).animate({top:"+=15px",right:"+=10px"},1500);
			$.float($("#bottle-bottle-"+i));
			setInterval("$.float($('#bottle-bottle-" + i +"'))",5400);
			i++;
			}
	});};
	k=1;
	var chk = function (){
		for(j=k;j<i;j++){
			if( $("#bottle-bottle-"+ j).position().left <= -30){
				$("#bottle-" + j).remove();
				k++;
				
			}
		}
	}
	
	setTimeout(stm,0);
	setInterval(stm,5500);
	setInterval(chk,5500);
	
	
	

	
});
