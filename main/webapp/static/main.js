$(function() {

    var div = $('.card-body');
    var ul = $('ul');
    var colors = [];
 
    $.getJSON('data.json', function(data) {
        $.each(data.colorDetected, function(i, f) {
            colors.push([f.color, f.time]);
        });
        addContent();
    });
 
    function addContent(e) {
        e.preventDefault();
        var hash = this.hash.replace('#','');
        div.html('');
        div.append('<div class="alert alert-primary" role="alert">' + colors[hash][0] + " Detected at: " + colors[hash][1] +'</div>');
        
    }
 
 });