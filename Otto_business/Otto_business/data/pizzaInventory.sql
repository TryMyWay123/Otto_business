CREATE DATABASE Inventory

CREATE TABLE Dough(PRIMARY KEY doughID int, doughName VARCHAR(255), quantity int, price int)
INSERT INTO Dough(doughID, doughName, quantity, price)
VALUES
(1, "Classic Dough", 30, 3.99),
(2, "Whole Wheat", 30, 4.49), 
(3, "Herb and Cheese", 30, 4.99),
(4, "Cauliflower", 30, 5.99),
(5, "Cheese Stuffed", 30, 6.99), 
(6, "Garlic crust", 30, 3.99)


CREATE TABLE Sauce(PRIMARY KEY sauceID int, sauceName VARCHAR(255), quantity int, price int)
INSERT INTO Sauce(sauceID, sauceName, quantity, price)
VALUES
(1, "Classic Sauce", 12, 2.99),
(2, "Pesto Sauce", 12, 4.99),
(3, "Alfredo Sauce", 12, 3.99),
(4, "BBQ", 12, 4.49),
(5, "Ranch", 12, 4.00),
(6, "Buffalo", 12, 3.99)


CREATE TABLE Cheese(PRIMARY KEY cheeseID int, cheeseName VARCHAR(255), quantity int, price int)
INSERT INTO Cheese(cheeseID, cheeseName, quantity, price)
VALUES
(1, "Mozzarella", 15, 3.99), 
(2, "Parmesan", 15, 3.49),
(3, "Cheddar", 15, 3.99), 
(4, "Provolone", 15, 4.49), 
(5, "Gouda", 15, 4.99), 
(6, "Pepper Jack", 15, 5.99),
(7, "Blue cheese", 15, 4.99)


CREATE TABLE Topping(PRIMARY KEY toppingID int, toppingName VARCHAR(255), quantity int, price int)
INSERT INTO Topping(toppingID, toppingName, quantity, price)
VALUES
(1, "Bell Peppers", 20, 1.99),
(2, "Onions", 20, 1.49),
(3, "Mushrooms", 20, 2.49),
(4, "Tomatoes", 20, 2.99),
(5, "Olives", 20, 2.49),
(6, "Spinach", 20, 2.99),
(7, "Arugula", 20, 3.49),
(8, "Zucchini", 20, 2.99),
(9, "Artichokes", 20, 3.99),
(10, "Eggplant", 20, 3.49),
(11, "Corn", 20, 2.99),
(12, "Pepperoni", 20, 3.99),
(13, "Sausage", 20, 4.49),
(14, "Ham", 20, 3.99),
(15, "Bacon", 20, 4.99),
(16, "Beef", 20, 3.99),
(17, "Chicken", 20, 4.49),
(18, "Anchovies", 20, 5.99),
(19, "Shrimp", 20, 6.99),
(20, "Pineapple", 20, 3.99),
(21, "Salami", 20, 4.99),
(22, "Prosciutto", 20, 5.99),
(23, "Turkey", 20, 4.49),
(24, "Pastrami", 20, 6.99),
(25, "Cajun Chicken", 20, 5.99), 
(26, "Capicola", 20, 5.99),
(27, "Chorizo", 20, 4.99),
(28, "Bresaola", 20, 6.99)





