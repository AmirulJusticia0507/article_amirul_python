from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint untuk membuat artikel baru
@app.route('/article/', methods=['POST'])
def create_article():
    data = request.json
    # Validasi data JSON
    if 'title' not in data or len(data['title']) < 20:
        return jsonify({'error': 'Title is required and must be at least 20 characters long'}), 400
    if 'content' not in data or len(data['content']) < 200:
        return jsonify({'error': 'Content is required and must be at least 200 characters long'}), 400
    if 'category' not in data or len(data['category']) < 3:
        return jsonify({'error': 'Category is required and must be at least 3 characters long'}), 400
    if 'status' not in data or data['status'] not in ['publish', 'draft', 'trash']:
        return jsonify({'error': 'Status is required and must be one of "publish", "draft", "trash"'}), 400
    
    # Proses penyimpanan artikel ke database
    
    return jsonify({'message': 'Article created successfully'}), 201

# Endpoint untuk menampilkan semua artikel dengan paging
@app.route('/article/<int:limit>/<int:offset>', methods=['GET'])
def get_articles(limit, offset):
    # Proses pengambilan artikel dari database dengan paging
    
    return jsonify(articles), 200

# Endpoint untuk menampilkan artikel berdasarkan ID
@app.route('/article/<int:id>', methods=['GET'])
def get_article(id):
    # Proses pengambilan artikel dari database berdasarkan ID
    
    return jsonify(article), 200

# Endpoint untuk mengubah artikel berdasarkan ID
@app.route('/article/<int:id>', methods=['PUT', 'PATCH'])
def update_article(id):
    data = request.json
    # Validasi data JSON
    if 'title' not in data or len(data['title']) < 20:
        return jsonify({'error': 'Title is required and must be at least 20 characters long'}), 400
    if 'content' not in data or len(data['content']) < 200:
        return jsonify({'error': 'Content is required and must be at least 200 characters long'}), 400
    if 'category' not in data or len(data['category']) < 3:
        return jsonify({'error': 'Category is required and must be at least 3 characters long'}), 400
    if 'status' not in data or data['status'] not in ['publish', 'draft', 'trash']:
        return jsonify({'error': 'Status is required and must be one of "publish", "draft", "trash"'}), 400
    
    # Proses pembaruan artikel di database
    # Misalnya, Anda dapat menggunakan SQLAlchemy untuk mengakses dan memperbarui data di database
    # Berikut adalah contoh menggunakan SQLAlchemy
    from models import Article  # Impor model Article, ganti dengan nama model yang sesuai
    article = Article.query.filter_by(id=id).first()  # Mengambil artikel dari database berdasarkan ID
    if article:
        article.title = data['title']
        article.content = data['content']
        article.category = data['category']
        article.status = data['status']
        # Menyimpan perubahan ke dalam database
        db.session.commit()
        return jsonify({'message': 'Article updated successfully'}), 200
    else:
        return jsonify({'error': 'Article not found'}), 404


# Endpoint untuk menghapus artikel berdasarkan ID
@app.route('/article/<int:id>', methods=['DELETE'])
def delete_article(id):
    # Proses penghapusan artikel dari database
    
    return jsonify({'message': 'Article deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
