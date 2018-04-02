# Librarian - documentation

# Preface
----------

*Dear Reader,*

***The following documentation provides onboard functionality of our service. The main goal is to focus on separate* ***views*** *and then split all information into* ***parts****, what is better for reader.*

***NB: For the faster navigation, please use left-sided navigation panel.*** *If you can not see it, just move your cursor to the left browser’s border.*
****
*Hope you enjoy the reading! 🙂 The Librarian’s team.*

# Semantics - outline
----------
1. Customer’s view
    1. **As non-Librarian**
      1. [*Registration and accessing system*](/doc/Librarian-documentation-t8uZbJ15rKtRBuOVqEuyZ#:h2=Registration-in-system)
      2. [*Manage my profile*](/doc/Librarian-documentation-t8uZbJ15rKtRBuOVqEuyZ#:h2=Manage-my-profile)
**      3. [*Surf & book*](/doc/Librarian-documentation-t8uZbJ15rKtRBuOVqEuyZ#:h2=Surf-&-Book)
      4. [*Tracking my orders*](/doc/Librarian-documentation-t8uZbJ15rKtRBuOVqEuyZ#:h2=Tracking-my-orders)
**      5. [*Get notifications*](/doc/Librarian-documentation-t8uZbJ15rKtRBuOVqEuyZ#:h2=Get-notifications)
    2. **As Librarian**
      1. [*Manage all documents*](/doc/Librarian-documentation-t8uZbJ15rKtRBuOVqEuyZ#:h2=Manage-all-documents)
**      2. [*Manage all users*](/doc/Librarian-documentation-t8uZbJ15rKtRBuOVqEuyZ#:h2=Manage-all-users)
**      3. [*Track and manage all orders*](/doc/Librarian-documentation-t8uZbJ15rKtRBuOVqEuyZ#:h2=Track-and-manage-all-orders)
2. Developer’s view
    1. **Frontend**
      1. [Technologies used in frontend](/doc/Librarian-documentation-t8uZbJ15rKtRBuOVqEuyZ#:h2=Technologies-used-in-frontend)
        1. *HTML & SASS & JS*
        2. *AngularJS*
      2. [Modular system](/doc/Librarian-documentation-t8uZbJ15rKtRBuOVqEuyZ#:h2=Modular-system)
      3. [System Administrator’s module](/doc/Librarian-documentation-t8uZbJ15rKtRBuOVqEuyZ#:h2=Administrator%E2%80%99s-module)
        1. *Managing site from administrator’s page*
    2. **Backend**
      1. [Technologies used in backend](/doc/Librarian-documentation-t8uZbJ15rKtRBuOVqEuyZ#:h2=Technologies-used-in-backend)
        1. *Django*
        2. *MySQL*
      2. [Client ↔ Server (as backend-side)](/doc/Librarian-documentation-t8uZbJ15rKtRBuOVqEuyZ#:h2=Client-server-behaviour)
        1. *Get requests from user*
        2. *Send responses on requests*
      3. [Server (as backend-side) ↔ DB](/doc/Librarian-documentation-t8uZbJ15rKtRBuOVqEuyZ#:h2=Server-as-backend-and-DB)
        1. *Manage all project data*
        2. *Perform changes on accepted queries*
      4. [Server (as backend-side) ↔ Server (as machine)](/doc/Librarian-documentation-t8uZbJ15rKtRBuOVqEuyZ#:h2=Server-as-backend-with-server-)
        1. *Routing of queries*
      5. [Server (as backend-side) ↔ Social networks](/doc/Librarian-documentation-t8uZbJ15rKtRBuOVqEuyZ#:h2=Server-as-backend-and-Social-N)
        1. *Telegram notifications*
    3. **Server (as machine)**
      1. [Domain delegation](/doc/Librarian-documentation-t8uZbJ15rKtRBuOVqEuyZ#:h2=Domain-Delegation)
        1. *URL access to routes*
        2. *HTTP → SSL*
      2. [Serving static files](/doc/Librarian-documentation-t8uZbJ15rKtRBuOVqEuyZ#:h2=Serving-static-files)
        1. *Access to www*
        2. *SSL encryption*


# 1. Customer’s view
----------
## I. As non-Librarian

**Registration in system**

----------

[Register](https://trainno.ru/auth/signup) in the system. **Be careful!** You need to register with your Telegram Username


![The registration process is quite simple - just one image describes all things here](https://d2mxuefqeaa7sj.cloudfront.net/s_148BE1924C6F9B99676949D405998FF012024E06BFEFFEC33752FA0C90457172_1522619683512_Screen+Shot+2018-04-02+at+00.53.24.png)


You also can [access system](https://trainno.ru/auth/login) in any time

![Type in your credentials - and that’s all](https://d2mxuefqeaa7sj.cloudfront.net/s_148BE1924C6F9B99676949D405998FF012024E06BFEFFEC33752FA0C90457172_1522619840853_Screen+Shot+2018-04-02+at+00.56.53.png)


**Manage my profile**

----------

This *dropdown menu* will be always on the top right corner of site whenever you logged in

![Dropdown menu](https://d2mxuefqeaa7sj.cloudfront.net/s_148BE1924C6F9B99676949D405998FF012024E06BFEFFEC33752FA0C90457172_1522620663618_Screen+Shot+2018-04-02+at+01.10.17.png)


You can manage [your profile](https://trainno.ru/user/profile) or open it from *dropdown menu*

![Your profile](https://d2mxuefqeaa7sj.cloudfront.net/s_148BE1924C6F9B99676949D405998FF012024E06BFEFFEC33752FA0C90457172_1522620462537_Screen+Shot+2018-04-02+at+01.07.30.png)


**Surf & Book**

----------

Let’s book a document: you can select any from [main page](https://trainno.ru/documents), you will see *document info*

![Document’s information](https://d2mxuefqeaa7sj.cloudfront.net/s_148BE1924C6F9B99676949D405998FF012024E06BFEFFEC33752FA0C90457172_1522621222868_Screen+Shot+2018-04-02+at+01.19.33.png)


You’re done! Move to the next step.

**Tracking my orders**

----------

When you click on button to order document, you will be on [my orders](https://trainno.ru/user/orders) page

![Your orders will be here](https://d2mxuefqeaa7sj.cloudfront.net/s_148BE1924C6F9B99676949D405998FF012024E06BFEFFEC33752FA0C90457172_1522621600555_Screen+Shot+2018-04-02+at+01.25.53.png)


From here you can see the statuses of all documents booked by you.

**Get notifications**

----------

Whenever state changes, you get following notification on **Telegram** by our *Librarian bot*.


![You will receive messages from our bot - all processes are automatic](https://d2mxuefqeaa7sj.cloudfront.net/s_148BE1924C6F9B99676949D405998FF012024E06BFEFFEC33752FA0C90457172_1522622172325_Screen+Shot+2018-04-02+at+01.35.57.png)




## II. As Librarian

All the features from non-librarian are available to the librarian, but also including following:

**Manage all documents**

----------

For librarian, all the documents will be available [here](https://trainno.ru/librarian/document-list):

![](https://d2mxuefqeaa7sj.cloudfront.net/s_148BE1924C6F9B99676949D405998FF012024E06BFEFFEC33752FA0C90457172_1522623174556_Screen+Shot+2018-04-02+at+01.51.07.png)


**Manage all users**

----------

Also, he can manage all registered users from [here](https://trainno.ru/librarian/user-list):

![](https://d2mxuefqeaa7sj.cloudfront.net/s_148BE1924C6F9B99676949D405998FF012024E06BFEFFEC33752FA0C90457172_1522623279563_Screen+Shot+2018-04-02+at+01.54.26.png)


**Track and manage all orders**

----------

As for librarian, he only able to accept and close orders or close preorders from [here](https://trainno.ru/librarian/order-list). 
All other stuff is fully auto-powered 🚀 

![In the overall](https://d2mxuefqeaa7sj.cloudfront.net/s_148BE1924C6F9B99676949D405998FF012024E06BFEFFEC33752FA0C90457172_1522623417228_Screen+Shot+2018-04-02+at+01.56.43.png)



![If librarian wants manage status](https://d2mxuefqeaa7sj.cloudfront.net/s_148BE1924C6F9B99676949D405998FF012024E06BFEFFEC33752FA0C90457172_1522623489462_Screen+Shot+2018-04-02+at+01.57.42.png)



![Then on Accept librarian will see this - accepted and return time](https://d2mxuefqeaa7sj.cloudfront.net/s_148BE1924C6F9B99676949D405998FF012024E06BFEFFEC33752FA0C90457172_1522624556501_Screen+Shot+2018-04-02+at+02.15.40.png)


And many more features. Next step is to see how this all works - from the developer’s view.


# 2. Developer’s view
----------


## I. Frontend

**Technologies used in frontend**

----------

In frontend we used standard technologies:

- **HTML**
- **SASS** (or SCSS)
- **JavaScript**

And the framework **AngularJS**.

The main goal and concept was to create fast, reactive and responsible design as *good as possible* in *less time*. That’s why we decided to use **AngularJS** instead of other frameworks.

**Modular system**

----------

The main idea in **AngularJS** is about using extendable modular system, what’s represented above.

![The simple modularity of AngularJS - Dashboard component](https://d2mxuefqeaa7sj.cloudfront.net/s_148BE1924C6F9B99676949D405998FF012024E06BFEFFEC33752FA0C90457172_1522625871571_Screen+Shot+2018-04-02+at+02.37.35.png)


And this module from other perspective - as graph:

![Dashboard Component as graph](https://d2mxuefqeaa7sj.cloudfront.net/s_148BE1924C6F9B99676949D405998FF012024E06BFEFFEC33752FA0C90457172_1522627122427_dashboard.png)


If you wish - full **Admin component** graph:

![Admin component as graph](https://d2mxuefqeaa7sj.cloudfront.net/s_148BE1924C6F9B99676949D405998FF012024E06BFEFFEC33752FA0C90457172_1522627159639_admin.png)


And so on. All components, services, models and other stuff here is in one hierarchy, what makes this system complete.

**Administrator’s module**

----------

All of the basic functional for *non-librarian users* and *librarians* were described in [Section 1](/doc/Librarian-documentation-t8uZbJ15rKtRBuOVqEuyZ#:uid=650884393734082920994096&h2=1.-Customer%E2%80%99s-view).

*But,*
One interesting feature allows administrator to manage the **DB** directly from the [Admin Panel](https://trainno.ru/admin/); Moreover, administrator’s admin page have more features than librarian’s. It can be accessed only if the module is accessible via URL, what describes this feature more in Section 3.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_148BE1924C6F9B99676949D405998FF012024E06BFEFFEC33752FA0C90457172_1522627953259_Screen+Shot+2018-04-02+at+03.11.25.png)

## II. Backend

**Technologies used in backend**

----------

We used following technologies in backend developing:

- **Python**
- **Django**
- **MySQL**

**Django** is powered by **Python**, in general that means that we can write extendable and production-ready systems in very fast and aesthetic way. 

**MySQL** is used as main DataBase (DB). We decided to use **MySQL** because it is quite simple and responsible on every change of our system, also very collaborative with **Django.**

In general, **Django** is also can be *modular*, but this modularity is not necessary - you can avoid separating classes of each component of system in the corresponding folders. Unfortunately, this is chaotic way to have one-layered hierarchy - and we think in this way too. So we separated all necessary classes in their folders, that you can see by visiting [our repository](https://github.com/slavagoreev/librarian) and go to *server* folder.

**Client-server behaviour**

----------

Client sends *packets, or* ***requests****, to perform an action, which will have an outgoing requests, also called* ***responses****, by a server.*

![Server get these requests as links](https://d2mxuefqeaa7sj.cloudfront.net/s_148BE1924C6F9B99676949D405998FF012024E06BFEFFEC33752FA0C90457172_1522628846290_Screen+Shot+2018-04-02+at+03.25.32.png)


The picture describes behaviour of client-server dialogue, as you can see, after the type of **request** and it’s link goes number, which describes type of **response**, as an example - first GET request were answered by server with **Response Code 200**. All response codes in segment **400**-**499** will be highlighted with red color - they represents bad behaviour, as example - **404** represents *Page Not Found*.

**Server as backend and DB**

----------

**Django** uses direct messages to DB - we configured *root access* to database for the **Django** platform, that it can manipulate it by it’s own terminal calls.

Example of DATABASES variable in *settings.py* of Django Server

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'librarian',
            'USER': DB_USERNAME,
            'PASSWORD': DB_PASSWORD,
            'HOST': SOCKET_FILE_DEST
        }
    }

**Server as backend with server as a machine**

----------

This is much more complicated topic. 
All corresponding things in detailed way about routing is written in Section 3 - Server as machine.

The thing is, we wrote in **Django** the routing system through corresponding endpoint - which, for server, as usual:

    python3 manage.py runserver trainno.ru:41000 &

The *host* (trainno.ru:41000) there is used to be the main route for server calls. URL’s routing are written in following way:

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('lmsinno.urls')),
    ]

These features help the server machine to do less things for the production.

**Server as backend and Social Networks**

----------

*Few words about Telegram.*

As you mentioned, there is *Telegram Username* used as required to register in our system. This feature is important because of how the *Telegram Policy* about authorising process goes - we cannot manage the list of registered users directly. Instead, we use *Telegram Usernames* to find their registration from the Telegram Route directly.

There is, if you haven’t accepted the authorisation that went from Telegram Popup window - you need to do it directly. There will be an option to open this window when you open the *Document Info* of some document listed in the main page. We apologise for that ‘feature’, and as fast Telegram updates their authorisation process - we will step forward to do changes in our system. The Telegram is used only to make your booking process more comfortable.

## III. Server (as machine)

**Domain Delegation**

----------

The way you use our system is simple, but the routing process is much more complicated. As you can see, we have [our own domain](https://trainno.ru) and you can surf on our site by accessing the link:

![The link to our service](https://d2mxuefqeaa7sj.cloudfront.net/s_148BE1924C6F9B99676949D405998FF012024E06BFEFFEC33752FA0C90457172_1522631614952_Screen+Shot+2018-04-02+at+04.13.21.png)


In that case we just bought the domain on name *trainno.ru*, then we found corresponding **hosting server** to allocate resources for our project - all the files of librarian repository are also stored in the hosting server too. The *domain* and *server* are connected via **DNS servers**.

Also, we guarantee the security of your dialogue with our server by providing instant **HTTPS**:

![The HTTPS certificate that is used for dialogue between your client and our server](https://d2mxuefqeaa7sj.cloudfront.net/s_148BE1924C6F9B99676949D405998FF012024E06BFEFFEC33752FA0C90457172_1522631926091_Screen+Shot+2018-04-02+at+04.17.48.png)


The server’s process to route **HTTP**→**HTTPS** queries is quite simple and used with **nginx**:

    server {
            listen 80;
            listen [::]:80;
            server_name trainno.ru;
    
            include /etc/nginx/snippets/letsencrypt.conf;
    
            location / {
                    return 301 https://trainno.ru$request_uri;
            }
    }
    
    server {
            server_name trainno.ru;
            listen 443 ssl http2 default_server;
            listen [::]:443 ssl http2 default_server ipv6only=on;
    
            ssl_certificate /etc/letsencrypt/live/www.trainno.ru/fullchain.pem;
            ssl_certificate_key /etc/letsencrypt/live/www.trainno.ru/privkey.pem;
            ssl_trusted_certificate /etc/letsencrypt/live/www.trainno.ru/fullchain.pem;
            include /etc/nginx/snippets/ssl.conf;
            
            index index.html;
            location / {
                    add_header X-Frame-Options SAMEORIGIN;
                    uwsgi_pass django;
                    proxy_pass http://trainno.ru:42000;
            }
            location /admin {
                    proxy_pass http://trainno.ru:41000;
            }
            location /static {
                    proxy_pass http://trainno.ru:41000/static;
            }
            location /api {
                    proxy_pass http://trainno.ru:41000/api;
            }
    }

**Serving static files**

----------

The **DNS** servers were provided by Yandex, so we can route through their servers and the site will be available to whole **www**.

SSL Encryption provided by Let’s Encrypt and used in **nginx** headers:

    ssl_certificate /etc/letsencrypt/live/www.trainno.ru/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/www.trainno.ru/privkey.pem;
    ssl_trusted_certificate /etc/letsencrypt/live/www.trainno.ru/fullchain.pem;


----------

That’s maybe not all, updates are coming….

