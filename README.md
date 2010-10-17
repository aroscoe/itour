Simple abstraction on the Bands in Town API.

Setup
-----

    $ git clone git://github.com/aroscoe/itour.git
    $ cd itour/
    itour $ git submodule update --init

Running Demos
-------------

### Command-Line

Using iTunes XML file

    itour/demos/cli $ ./main.py -f ~/Music/iTunes/iTunes\ Music\ Library.xml

Add your own artists by hand

    itour/demos/cli $ ./main.py -a "weezer, dredg"

### Frameworks

Install the necessary modules to run Django (1.2.3) or Web.py (0.34).

    itour $ pip install -r REQUIREMENTS

#### Django

    itour/demos/dj $ ./manage.py runserver

#### Web.py

    itour/demos/webpy $ ./code.py 8000
    
### Request/Response

Send a post with artists and a location

    $ curl http://localhost:8000 -d location='Brooklyn, NY' -d artists='dredg'

JSON response
    
    [
        {
            "artists": [
                {
                    "mbid": "7b2f87f6-db90-464e-a27a-deb4f7219e90", 
                    "name": "dredg", 
                    "url": "http://www.bandsintown.com/dredg"
                }
            ], 
            "datetime": "2010-11-27T19:00:00", 
            "id": 3829473, 
            "on_sale_datetime": null, 
            "ticket_status": "available", 
            "ticket_url": "http://www.bandsintown.com/event/3829473/buy_tickets", 
            "url": "http://www.bandsintown.com/event/3829473", 
            "venue": {
                "city": "New York", 
                "country": "United States", 
                "id": 376815, 
                "latitude": 40.7141667, 
                "longitude": -74.006388900000005, 
                "name": "The Fillmore New York at Irving Plaza", 
                "region": "NY", 
                "url": "http://www.bandsintown.com/venue/376815"
            }
        }
    ]
