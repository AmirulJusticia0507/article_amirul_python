import mysql.connector

# Menghubungkan ke database MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_post_article_amirul"
)

# Membuat kursor
cursor = conn.cursor()

# Membaca data dari tabel posts
cursor.execute("""
    SELECT
      `id`,
      `Title`,
      `Content`,
      `Category`,
      `Created_date`,
      `update_date`,
      `Status`
    FROM
      `posts`
    LIMIT 0, 1000;
""")

# Membuat tabel baru di database artikel_amirul
cursor.execute("""
    CREATE TABLE IF NOT EXISTS article (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        content TEXT NOT NULL,
        category VARCHAR(255) NOT NULL,
        created_date DATETIME,
        update_date DATETIME,
        status ENUM('publish', 'draft', 'trash') NOT NULL
    );
""")

# Menutup koneksi
cursor.close()
conn.close()
