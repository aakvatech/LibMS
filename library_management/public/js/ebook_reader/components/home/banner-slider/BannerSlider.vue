<!-- template for the slider component -->
<template>
  <div class="banner-section">
    <div class="container">
      <div class="flexslider">
        <ul class="slides">
          <li>
            <img src="/files/banner.png" />
          </li>
          <!-- <li>
                <img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/5689/grooves.jpg" />
            </li>
            <li>
                <img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/5689/arch.jpg" />
            </li>
            <li>
                <img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/5689/sunset.jpg" />
            </li> -->
        </ul>
      </div>
    </div>
  </div>

</template>
<script>
// // define slider component
// Vue.component('img-slider', {
//     template: '#img-slider-template',
//     replace: true
// })
// // boot up demo
// new Vue({
//     el: '#demo'
// })
</script>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
<script defer src="http://flexslider.woothemes.com/js/jquery.flexslider.js"></script>
<script>
$(function(){
  SyntaxHighlighter.all();
});
$(window).load(function(){
  $('.flexslider').flexslider({
    animation: "slide",
    start: function(slider){
      $('body').removeClass('loading');
    }
  });
});
</script>
<style scoped>
@import "./style.css";
</style>
