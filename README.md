# covid-19-api
---
This API is capable of fetching Coronavirus Cases country wise and for indian states.
---
## SOURCES

[WORLDOMETER](https://www.worldometers.info/coronavirus) for country data

[Ministry of Health and Family Welfare(GOI)](https://www.mygov.in/covid-19) for Indian state's data

---

### Show some :heart: and :star: the repo to support the project

---
## Usage
Make a get request for the type of data you want

For country data : https://covid19indapi.herokuapp.com/country

For Indian state's data : https://covid19indapi.herokuapp.com/india

---
## Response Format

for indian data
```JSON
{
  "data": [
    {
      "active": "0",
      "confirmed": "33",
      "deaths": "0",
      "recovered": "33",
      "state": "Andaman and Nicobar"
    },
    {
      "active": "1341",
      "confirmed": "3783",
      "deaths": "64",
      "recovered": "2378",
      "state": "Andhra Pradesh"
    }
   ],
  "success": true
}
```
for country data

```JSON
{
  "data": [
    {
      "active_cases": "+1,380",
      "country": "USA",
      "new_cases": "+6,136",
      "total_cases": "1,865,459",
      "total_deaths": "107,313 ",
      "total_recovered": "616,796"
    },
    {
      "active_cases": "",
      "country": "Brazil",
      "new_cases": "+1,328",
      "total_cases": "530,733",
      "total_deaths": "30,079  ",
      "total_recovered": "211,080"
    },
    {
      "active_cases": "+11,108",
      "country": "Russia",
      "new_cases": "+8,863",
      "total_cases": "423,741",
      "total_deaths": "5,037 ",
      "total_recovered": "186,985"
    },
    {
      "active_cases": "N/A",
      "country": "Spain",
      "new_cases": "",
      "total_cases": "286,718",
      "total_deaths": "27,127 ",
      "total_recovered": "N/A"
    }
   ],
  "success": true
}
```

---
## Setup

Install all dependencies listed in *requirements.txt* file. 

1. To install all dependencies run - 

    ```bash
    $ sudo -H pip3 install -r requirements.txt
    ```

2. Start the server

    ```bash 
    $ python app.py
    ```
---
#### :star: the Repo if you liked it and do mention this repo if you are using it in your project.. :D

# © [IFRAHUR RAHMAN](https://ifrahur.me/)
