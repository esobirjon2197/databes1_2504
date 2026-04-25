CREATE TABLE IF NOT EXISTS users(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	username REAL,
	email REAL UNIQUE,
	age INTEGER CHECK(age >=18  AND age <= 90),
	balnce INTEGER CHECK(balnce >= 0),
	status TEXT CHECK (status IN ('active', 'blocked'))
	
);

CREATE Table IF NOT EXISTS products(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	sku REAL UNIQUE,
	name TEXT NOT NULL,
	price INTEGER CHECK (price >= 0),
	stock INTEGER CHECK (stock >= 0),
	discount_pct INTEGER CHECK (discount_pct >= 0 AND discount_pct < 100)
);


CREATE Table IF NOT EXISTS orders(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	order_code REAL,
	user_id INTEGER,
	produck_id INTEGER,
	quantfily INTEGER CHECK (quantfily >= 1),
	satus  TEXT CHECK (satus IN ('done', 'shipped', 'pending'))
);


CREATE Table IF NOT EXISTS reviews(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	users_id INTEGER,
	producks_id INTEGER,
	reting INTEGER CHECK (reting >= 1 AND reting <= 5),
	comment TEXT CHECK (comment >= 10),
	helpful_count INTEGER CHECK (helpful_count >= 0)
);


CREATE Table IF NOT EXISTS tickets(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	us_id INTEGER,
	subject TEXT CHECK (subject >= 5),
	prioritfy TEXT CHECK (prioritfy IN ('high', 'medium', 'low')),
	sts TEXT CHECK (sts IN ('open', 'in_progress', 'closed')),
	creat_id REAL
);


INSERT INTO users
(username, email, age, balnce, status)
VALUES
('Ali_dev', 'ali@maill.uz', 25, 320000, 'active'),
('nilufar', 'nilu@gmail.com', 22, 0, 'blocked'),
('sardor_x', 'sardor@box.com', 31, 1500000, 'active');


INSERT INTO products
(sku, name, price, stock, discount_pct)
VALUES
('Shoe-001', 'Adidas', 850000, 12, 10),
('Phon-002', 'Samsung', 24900000, 5, 0),
('Book-003', 'Clean code', 12000, 30, 25);


INSERT INTO orders
(order_code, user_id , produck_id, quantfily, satus)
VALUES
('ORD-2026-01', 1, 2, 1, 'done'),
('ORD-2026-02', 2, 4, 2, 'shipped'),
('ORD-2026-03', 1, 3, 5, 'done');


INSERT INTO reviews
(users_id, producks_id, reting, comment, helpful_count)
VALUES
(1, 2, 5, 'Juda zor telefon', 14),
(3, 4, 4, 'Sifatli quloqchin', 7),
(4, 3, 3, 'Ortacha kitob', 2);


INSERT INTO tickets
(us_id, subject, prioritfy, sts, creat_id)
VALUES
(2, 'Tolov amalga oshdi', 'high', 'open', '2026-03-01'),
(1, 'Buyurtma kelmadi', 'medium', 'in_progress', '2026-03-05'),
(4, 'Parol unitildi', 'low', 'closed', '2026-03-10'); 




