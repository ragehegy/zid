**Stack used:**
- Python/Django
- Django Rest Framework (DRF)
- MySQL
- REST API
- xhtml2pdf
- PyTest & pytest-django


**Setting up:**
- From the root dir in the project, Create and activate a virtual environemt to setup the necessary packages:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```
- Now the new virtual environment should be created, next we install the required packages list in `requriements.txt` via `pip` or `pip3`:
  ```
  pip install -r requirements.txt
  ```
- Change the username and password in `.env` file with your MySQL DB user credentials, DB name, host and port.
- To initialize the DB and create the couriers DB tables we need to make and run the project migrations: 
  ```
  python manage.py makemigrations couriers
  python manage.py migrate couriers
  ```` 
- Seed sample couriers data to be able to use a valid courier:
  ```
  python manage.py dumpsampledata
  ```


**Steps to run the app:**
- Now start the server by running the command `python manage.py runserver`. The server should be running now on http://127.0.0.1:8000/.
- The couriers endpoint is served on `/couriers`.
- Create a simple GET request to `/couriers` to fetch the whole couriers data.
- The shipments endpoint is served on `/shipments`.

**API Features:**
- Create Courier
    - URL: `http://127.0.0.1:8000/couriers`
    - Method: `POST`
    - Payload sample: 
        ```
        {
            "name": "<string>",
            "url": "<valid url>",
            "shipment_cancellable": <boolean>
        }
        ```

- List Couriers
    - URL: `http://127.0.0.1:8000/couriers`
    - Method: `GET`

- Retrieve Courier by ID
    - URL: `http://127.0.0.1:8000/couriers/<UUID>`
    - Method: `GET`

- Create Waybill(POST Shipment)
    - URL: `http://127.0.0.1:8000/shipments/`
    - Method: `POST`
    - Payload sample: 
        ```
        {
            "courier_id": "<UUID>",
            "status": "<str>",
            "tracking_id": "<str>",
            "sender": "<str>",
            "recipient": "<str>",
            "pickup_location": "<str>",
            "delivery_location": "<str>",
            "current_location": "<str>",
            "charges": "<float>"
        }
        ```

- Print Waybill
    - URL: `http://127.0.0.1:8000/shipments/<UUID>/print`
    - Method: `GET`

- Track Shipment Status(Retrieve Shipment)
    - URL: `http://127.0.0.1:8000/shipments/<UUID>/track`
    - Method: `GET`

- Cancel Shipment (if available)
    - URL: `http://127.0.0.1:8000/shipments/<UUID>/cancel/`
    - Method: `PATCH`


**Sample cURL requests:**

- *CREATE NEW WAYBILL*
    ```
    curl --location --request GET 'http://127.0.0.1:8000/metrics/?date__lte=2017-06-01&sum=impressions&sum=clicks&group=channel&group=country&sort_by=-clicks' \
    --header 'Cookie: csrftoken=wIN6rvACTKdZ6Cr6hvEM9yOdygzRcxXER57XSGfg9xZf1rM3Zqphw74YY0k6dPXd'
    ```

- *Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.*
    ```
    curl --location --request GET 'http://127.0.0.1:8000/metrics?date__lte=2017-05-30&sum=installs&date__gte=2017-05-01&os=IOS&group=date&sort_by=date' \
    --header 'Cookie: csrftoken=wIN6rvACTKdZ6Cr6hvEM9yOdygzRcxXER57XSGfg9xZf1rM3Zqphw74YY0k6dPXd'
    ```

- *Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.*
    ```
    curl --location --request GET 'http://127.0.0.1:8000/metrics/?date=2017-06-01&sum=revenue&sort_by=-revenue&country=US&group=os' \
    --header 'Cookie: csrftoken=wIN6rvACTKdZ6Cr6hvEM9yOdygzRcxXER57XSGfg9xZf1rM3Zqphw74YY0k6dPXd'
    ```

- *Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order.*
    ```
    curl --location --request GET 'http://127.0.0.1:8000/metrics/?sort_by=-CPI&sum=spend&group=country&group=channel&cpi=true&country=CA' \
    --header 'Cookie: csrftoken=wIN6rvACTKdZ6Cr6hvEM9yOdygzRcxXER57XSGfg9xZf1rM3Zqphw74YY0k6dPXd'
    ```