# Car Price Predictor
> Made by Aayush Jain
* Created a tool that helps people to know the resale value of the car based on KMs, year in which it was bought, model of car and fuel type.
* Scrapped data using python library beautiful soup.
* Car price prediction includes features such as KMs, year in which it was bought, model of car and fuel type.
* Model uses Linear Regression.
* Django and Ionic Framework for the web application.

## Code and Resources used:
* **Python Version:** 3.7
* **Packages:** pandas, numpy, sklearn, matplotlib, beautiful soup, django, pickle

## Web Scrapping:
The dataset includes 3609 data regarding the car.It contains following information:
* Price
* Model
* Year
* Fuel
* Milage

## EDA:
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights:
![Bar Graph](https://github.com/Darkshadow9799/CarPredictor/blob/master/bar%20graph.png)

## Model Building:
First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.

## Model Performance:
The model accuracy is: 88%.

## Produtionization:
In this step, I build the Django Framework and Ionic Framework for building the fully featured site.

## Technology:
### Frameworks:
* **Django Framework**
* **Ionic Framework**
### Languages:
* **Python**
* **Javascript**

## Huge Thanks:
* Sagar Patel: https://github.com/codesagar
* Parth Mistry: https://github.com/m-prth
