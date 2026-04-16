from flask import Blueprint

book_bp = Blueprint('book_routes', __name__)

@book_bp.route('/', methods=['GET'])
@book_bp.route('/books', methods=['GET'])
def list_books():
    """
    輸入: 無
    處理邏輯: 查詢系統中所有已登記書籍與最新動態
    輸出: 渲染 templates/books/index.html
    """
    pass

@book_bp.route('/books/search', methods=['GET'])
def search_books():
    """
    輸入: URL query string, 例: ?q=關鍵字
    處理邏輯: 查詢符合關鍵字的書籍
    輸出: 渲染 templates/books/search.html
    """
    pass

@book_bp.route('/books/add', methods=['GET', 'POST'])
def add_book():
    """
    GET: 
      處理邏輯: 顯示新增表單
      輸出: 渲染 templates/books/add.html
    POST: 
      處理邏輯: 接收表單內容並建立 Book，失敗則報錯
      輸出: 成功後重導向
    """
    pass

@book_bp.route('/books/<int:id>', methods=['GET'])
def book_detail(id):
    """
    輸入: 書籍的 id
    處理邏輯: 取得單本書籍與它所有的心得、評分資料
    輸出: 渲染 templates/books/detail.html (404 找不到書籍時報錯)
    """
    pass
