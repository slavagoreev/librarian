// To run data import, run django server on port 80 and then run:
// $ npm install -g querystring http fs
// $ node ./dataset_loader.js


var querystring = require('querystring');
var http = require('http');
var fs = require('fs');

const possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
function post(dataset) {
    // Build the post string from an object
    var post_data = querystring.stringify(dataset);
    //console.log(post_data)
    // An object of options to indicate where to post to
    var post_options = {
        host: 'localhost',
        port: '8000',
        path: '/api/documents/',
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': Buffer.byteLength(post_data),
            'Bearer': "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJlbWFpbCI6InNsYXZhZ29yZWV2QHJlZXNwYWNlLnJ1Iiwicm9sZSI6MiwiZXhwIjoxNTE5NTA1NDMyLCJvcmlnX2lhdCI6MTUxODkwMDYzMn0.h8a3I-ryQcBhuPUTdCTG2ccEgRzxBvpoE5FUn-iWy3s"
        }
    };
    //console.log (post_data)
    let post_req = http.request(post_options, function(res) {
        res.setEncoding('utf8');
        res.on('data', function (data) {
            try {
                data = JSON.parse(data);
            }
            catch (e) {
                return null
            }
            if (data.data && data.data.document_id) {
                console.log (`Document #${data.data.document_id} added`);
                post_options.path = '/api/copy/';
                for (let i = 0; i < Math.ceil(Math.random() * 3); i++) {
                    setTimeout(() => {
                        let copy = {
                            document: data.data.document_id,
                            status: 0,
                            place_hall_number: Math.ceil(Math.random() * 10),
                            place_shelf_letter: possible.charAt(Math.floor(Math.random() * possible.length))
                        };
                        let copy_req = http.request(post_options);
                        let copy_data = querystring.stringify(copy);
                        copy_req.write(copy_data);
                        copy_req.end();
                    }, 100*i);
                }
            }
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
        let i = 432;
        let int = setInterval(function () {
            books[i].publisher = (books[i].publisher) ? books[i].publisher : "Innopolis library";
            books[i].authors = (books[i].authors) ? books[i].authors.join(",") : "";
            books[i].description = books[i].description ? books[i].description : "";
            books[i].is_reference = (Math.random() * 100) < 3;
            books[i].is_bestseller = !books[i].is_reference && (Math.random() * 100) < 5;
            post(books[i]);
            if (i > books.length - 3)
                clearInterval(int);
            i++;
        }, 500)
    }
    else {
        console.log("No data to post");
        process.exit(-1);
    }
});