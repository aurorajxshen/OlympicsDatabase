import sqlite3

# 连接到SQLite数据库
conn = sqlite3.connect('olympics.db')
cursor = conn.cursor()

# 定义数据
dishes_data = [
    (1896, "Athens", "Local Greek Cuisine", "Traditional foods likely included lamb, olives, and bread, although specific dishes are not well-documented."),
    (1900, "Paris", "French Cuisine", "Featuring classics such as coq au vin and baguettes with various cheeses."),
    (1904, "St. Louis", "American BBQ", "Typical American foods like BBQ meats and apple pie were likely featured."),
    (1908, "London", "British Classics", "Dishes such as roast beef and Yorkshire pudding."),
    (1912, "Stockholm", "Scandinavian Cuisine", "Likely included dishes such as gravlax (cured salmon) and Swedish meatballs."),
    (1920, "Antwerp", "Belgian Specialties", "Mussels with fries and Belgian waffles."),
    (1924, "Paris", "French Gourmet", "High-quality French dishes like escargot and bouillabaisse."),
    (1932, "Los Angeles", "American Variety", "Featuring dishes such as hamburgers and hot dogs."),
    (1936, "Berlin", "German Cuisine", "Dishes like bratwurst and sauerkraut."),
    (1948, "London", "Post-war British Cuisine", "Simple, hearty meals such as shepherd's pie."),
    (1952, "Helsinki", "Finnish Cuisine", "Dishes like salmon soup and Karelian pasties."),
    (1956, "Melbourne", "Australian BBQ", "Featuring grilled meats and seafood."),
    (1960, "Rome", "Italian Classics", "Dishes like pasta carbonara and pizza margherita."),
    (1964, "Tokyo", "Japanese Cuisine", "Rice balls, sushi, and tempura."),
    (1968, "Mexico City", "Mexican Cuisine", "Tacos, enchiladas, and mole."),
    (1972, "Munich", "German Cuisine", "Pretzels, sausages, and beer."),
    (1976, "Montreal", "Canadian Fare", "Poutine and maple syrup-based dishes."),
    (1980, "Moscow", "Russian Cuisine", "Borscht and pelmeni."),
    (1984, "Los Angeles", "Diverse American Cuisine", "Featuring foods like California rolls and Tex-Mex dishes."),
    (1988, "Seoul", "Korean Cuisine", "Kimchi, bulgogi, and bibimbap."),
    (1992, "Barcelona", "Spanish Cuisine", "Tapas and paella."),
    (1996, "Atlanta", "Southern American Cuisine", "Fried chicken and peach cobbler."),
    (2000, "Sydney", "Australian Cuisine", "Barbecued prawns and lamingtons."),
    (2004, "Athens", "Greek Cuisine", "Souvlaki and baklava."),
    (2008, "Beijing", "Chinese Cuisine", "Peking duck, dim sum, and hotpot."),
    (2012, "London", "British Classics", "Fish and chips, roast dinners, and English breakfast."),
    (2016, "Rio", "Brazilian Cuisine", "Feijoada and pão de queijo."),
    (2020, "Tokyo", "Japanese Cuisine", "Sushi, ramen, and kaiseki."),
    (2022, "Beijing", "Chinese and International Cuisine", "Stir-fried beef, sweet and sour spare ribs, and various Western dishes like pizza and pasta."),
    (2024, "Paris", "French Gourmet", "Chicken tandir by Arkame Benallal, poached egg croissant with artichoke cream, goat cheese, and truffle by Amandine Chaignot, smoked salted hake with tapioca in a veggie bouillon by Alexandre Mazzia, almado-style bread salad by Stéphane Chicheri, and zaatar sweet potato with hummus and chimichurri by Charles Guilloy.")
]

# 插入数据
cursor.executemany('''
INSERT INTO SignatureDishes (year, city, cuisine, dishes) VALUES (?, ?, ?, ?)
''', dishes_data)

# 提交更改并关闭连接
conn.commit()
conn.close()
