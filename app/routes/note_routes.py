from flask import Blueprint

note_bp = Blueprint('note_routes', __name__)

@note_bp.route('/books/<int:id>/notes/add', methods=['GET', 'POST'])
def add_note(id):
    """
    GET: 
      處理邏輯: 確認書籍存在，渲染表單
      輸出: templates/notes/add.html
    POST: 
      處理邏輯: 接收評分、心得、標籤資料，建立 Note 並關聯至書籍
      輸出: 成功後重導向至 /books/<id>
    """
    pass

@note_bp.route('/tags/<string:tag_name>', methods=['GET'])
def list_by_tag(tag_name):
    """
    輸入: URL 變數 tag_name
    處理邏輯: 查詢含該標籤的所有書籍和心得
    輸出: 渲染 templates/tags/index.html
    """
    pass
