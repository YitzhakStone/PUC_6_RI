$(document).ready(function () {

    var access_token = "975448585.61ec9f0.3686d8aa7c0049389e9d9fb0f877092e"
        access_parameters = {
            access_token: access_token
        };

    var form = $('#tagsearch');
    form.on('submit', function(ev) {
        ev.preventDefault();
        var q = this.tag.value;
        if(q.length) {
            //console.log(q);
            grabImages(q, 40, access_parameters);
        }
    });

    function grabImages(tag, count, access_parameters) {
        var instagramUrl = 'https://api.instagram.com/v1/tags/' + tag + '/media/recent?callback=?&count=' + count;
        $.getJSON(instagramUrl, access_parameters, onDataLoaded);
    }

    function onDataLoaded(instagram_data) {
        var target = $("#target");
        //console.log(instagram_data);
        if (instagram_data.meta.code == 200) {
            var photos = instagram_data.data;
            //console.log(photos);
            if (photos.length > 0) {
                target.empty();
                for (var key in photos) {
                    var photo = photos[key];
                    target.append('<a href="' + photo.link + '"><img src="' + photo.images.thumbnail.url + '"></a>')
                }
            } else {
                target.html("nothing found");
            }
        } else {
            var error = instagram_data.meta.error_message;
            target.html(error);
        }
    }

    grabImages('information', 40, access_parameters);

});