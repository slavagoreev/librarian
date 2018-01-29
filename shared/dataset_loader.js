// To run data import, run django server on port 80 and then run:
// $ npm install -g querystring http fs
// $ node ./dataset_loader.js


var querystring = require('querystring');
var http = require('http');
var fs = require('fs');

function post(dataset) {
    // Build the post string from an object
    var post_data = querystring.stringify(dataset);
    //console.log(post_data)
    // An object of options to indicate where to post to
    var post_options = {
        host: 'localhost',
        port: '80',
        path: '/document/',
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': Buffer.byteLength(post_data)
        }
    };
    //console.log (post_data)
    var post_req = http.request(post_options, function(res) {
        res.setEncoding('utf8');
        res.on('data', function (chunk) {
            console.log('Response: ' + chunk);
        });
    });
    post_req.write(post_data);
    post_req.end();

}

// This is an async file read
fs.readFile('./dataset.json', 'utf-8', function (err, data) {
    if (err) {
        console.log("FATAL An error occurred trying to read in the file: " + err);
        process.exit(-2);
    }
    if (data) {
        let books = JSON.parse(data).items;
        let i = 0;
        setInterval(function () {
            books[i].publisher = (books[i].publisher) ? books[i].publisher : "Innopolis library";
            books[i].authors = (books[i].authors) ? books[i].authors.join(",") : "";
            books[i].description = books[i].description ? books[i].description : "";
            post(books[i]);
            i++;
        }, 200)
    }
    else {
        console.log("No data to post");
        process.exit(-1);
    }
});