$(window).scroll(function(){
    $('nav').toggleClass('change', $(this).scrollTop() > 300);
});



$(document).scroll(function(){
    var st = $(this).scrollTop();

    $(section).each(function() {
        if(st > $(this).offset().top && st <= $(this).offset().top + $(this).height() ){                    
            var id = $(this).attr('id');
            $('a[href="#'+id+'"]').addClass('active');
        }else{
            var id = $(this).attr('id');
            $('a[href="#'+id+'"]').removeClass('active');   
        }   
    });

});

$(document).ready((function(){!function(){if("requestAnimationFrame"in window&&!/Mobile|Android/.test(navigator.userAgent)){var e=[];if($("[data-bs-parallax-bg]").each((function(){var i=$(this),s=$("<div>");s.css({backgroundImage:i.css("background-image"),backgroundSize:"cover",backgroundPosition:"center",position:"absolute",height:"200%",width:"100%",top:0,left:0,zIndex:-100}),s.appendTo(i),e.push(s[0]),i.css({position:"relative",background:"transparent",overflow:"hidden"})})),e.length){var i,s=[];$(window).on("scroll resize",n),n()}}function n(){s.length=0;for(var n=0;n<e.length;n++){var a=e[n].parentNode.getBoundingClientRect();a.bottom>0&&a.top<window.innerHeight&&s.push({rect:a,node:e[n]})}cancelAnimationFrame(i),s.length&&(i=requestAnimationFrame(t))}function t(){for(var e=0;e<s.length;e++){var i=s[e].rect,n=s[e].node,t=Math.max(i.bottom,0)/(window.innerHeight+i.height);n.style.transform="translate3d(0, "+-50*t+"%, 0)"}}}()})),jQuery(document).ready((function(e){var s,n;function t(i){var s=r(i);if(i.parents(".cd-headline").hasClass("type")){var n=i.parent(".cd-words-wrapper");n.addClass("selected").removeClass("waiting"),setTimeout((function(){n.removeClass("selected"),i.removeClass("is-visible").addClass("is-hidden").children("i").removeClass("in").addClass("out")}),500),setTimeout((function(){a(s,150)}),1300)}else if(i.parents(".cd-headline").hasClass("letters")){var l=i.children("i").length>=s.children("i").length;!function i(s,n,a,d){s.removeClass("in").addClass("out"),s.is(":last-child")?a&&setTimeout((function(){t(r(n))}),2500):setTimeout((function(){i(s.next(),n,a,d)}),d);if(s.is(":last-child")&&e("html").hasClass("no-csstransitions")){var l=r(n);o(n,l)}}(i.find("i").eq(0),i,l,50),d(s.find("i").eq(0),s,l,50)}else i.parents(".cd-headline").hasClass("clip")?i.parents(".cd-words-wrapper").animate({width:"2px"},600,(function(){o(i,s),a(s)})):i.parents(".cd-headline").hasClass("loading-bar")?(i.parents(".cd-words-wrapper").removeClass("is-loading"),o(i,s),setTimeout((function(){t(s)}),3800),setTimeout((function(){i.parents(".cd-words-wrapper").addClass("is-loading")}),800)):(o(i,s),setTimeout((function(){t(s)}),2500))}function a(e,i){e.parents(".cd-headline").hasClass("type")?(d(e.find("i").eq(0),e,!1,i),e.addClass("is-visible").removeClass("is-hidden")):e.parents(".cd-headline").hasClass("clip")&&e.parents(".cd-words-wrapper").animate({width:e.width()+10},600,(function(){setTimeout((function(){t(e)}),1500)}))}function d(e,i,s,n){e.addClass("in").removeClass("out"),e.is(":last-child")?(i.parents(".cd-headline").hasClass("type")&&setTimeout((function(){i.parents(".cd-words-wrapper").addClass("waiting")}),200),s||setTimeout((function(){t(i)}),2500)):setTimeout((function(){d(e.next(),i,s,n)}),n)}function r(e){return e.is(":last-child")?e.parent().children().eq(0):e.next()}function o(e,i){e.removeClass("is-visible").addClass("is-hidden"),i.removeClass("is-hidden").addClass("is-visible")}e(".cd-headline.letters").find("b").each((function(){var s=e(this),n=s.text().split(""),t=s.hasClass("is-visible");for(i in n)s.parents(".rotate-2").length>0&&(n[i]="<em>"+n[i]+"</em>"),n[i]=t?'<i class="in">'+n[i]+"</i>":"<i>"+n[i]+"</i>";var a=n.join("");s.html(a).css("opacity",1)})),s=e(".cd-headline"),n=2500,s.each((function(){var i=e(this);if(i.hasClass("loading-bar"))n=3800,setTimeout((function(){i.find(".cd-words-wrapper").addClass("is-loading")}),800);else if(i.hasClass("clip")){var s=i.find(".cd-words-wrapper"),a=s.width()+10;s.css("width",a)}else if(!i.hasClass("type")){var d=i.find(".cd-words-wrapper b"),r=0;d.each((function(){var i=e(this).width();i>r&&(r=i)})),i.find(".cd-words-wrapper").css("width",r)}setTimeout((function(){t(i.find(".is-visible").eq(0))}),n)}))}));

if($(window).height() > $("body").height()){
$("footer").css("position", "fixed");
} else {
$("footer").css("position", "static");
}

window.onload = function() {
    lax.setup() // init
    
    const updateLax = () => {
    lax.update(window.scrollY)
    window.requestAnimationFrame(updateLax)
    }
    
    window.requestAnimationFrame(updateLax)
    }