# 讀書筆記本 - 路由設計文件 (API Design)

## 1. 路由總覽表格

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| --- | --- | --- | --- | --- |
| 首頁 / 書籍列表 | GET | `/` 或 `/books` | `books/index.html` | 顯示所有已紀錄的書籍與最近動態 |
| 搜尋書籍 | GET | `/books/search` | `books/search.html` | 透過 query 參數 `?q=` 搜尋書籍 |
| 新增書籍頁面 | GET | `/books/add` | `books/add.html` | 顯示新增書籍表單 |
| 建立書籍資料 | POST | `/books/add` | — | 接收表單並存入 DB，完成後重導向至首頁或書籍詳情 |
| 書籍詳情與心得 | GET | `/books/<int:id>` | `books/detail.html` | 顯示單筆書籍及該書的心得、評分列表 |
| 撰寫心得頁面 | GET | `/books/<int:id>/notes/add` | `notes/add.html` | 顯示特定書籍的撰寫心得表單 |
| 新增心得資料 | POST | `/books/<int:id>/notes/add` | — | 將表單心得寫入 DB 並重導向回書籍詳情頁 |
| 依標籤探索書籍 | GET | `/tags/<string:tag_name>` | `tags/index.html` | 顯示擁有特定標籤的所有書籍與筆記 |

## 2. 每個路由的詳細說明

### 2.1 書籍相關路由 (book_routes.py)

**首頁 / 書籍列表**
*   **輸入**：無
*   **處理邏輯**：查詢所有 `Book` 以及關聯的最新動態。
*   **輸出**：渲染 `books/index.html`。
*   **錯誤處理**：若無資料則顯示空狀態提示。

**搜尋書籍**
*   **輸入**：URL 參數 `?q=關鍵字`。
*   **處理邏輯**：使用關鍵字查詢 `Book` 的書名或其他欄位。
*   **輸出**：渲染 `books/search.html`。
*   **錯誤處理**：無參數或查無結果時，回傳相應提示文字並顯示無結果。

**新增書籍與建立資料**
*   **輸入 (GET)**：無。
*   **輸出 (GET)**：渲染 `books/add.html` 表單頁面。
*   **輸入 (POST)**：表單欄位（書名、作者等）。
*   **處理邏輯 (POST)**：建立新的 `Book` 資料並寫入 SQLite。
*   **輸出 (POST)**：成功後，重導向至 `/books/<int:id>` (該筆新增書籍之詳細頁面) 或首頁。
*   **錯誤處理**：若書名為空或其他必填驗證失敗，重新渲染表單並顯示錯誤訊息。

**書籍詳情與心得列表**
*   **輸入**：URL 變數 `<id>`。
*   **處理邏輯**：以 ID 查詢 `Book` 以及屬於它所有的 `Note` 與關聯 `Tag`。
*   **輸出**：渲染 `books/detail.html`。
*   **錯誤處理**：若 ID 查無對應書籍，回傳 HTTP 404 狀態碼與對應的錯誤頁面。

### 2.2 筆記相關路由 (note_routes.py)

**撰寫與新增心得資料**
*   **輸入 (GET)**：URL 變數 `<id>` (對應書籍 id)。
*   **處理邏輯 (GET)**：確認該筆書籍是否存在。
*   **輸出 (GET)**：存在則渲染 `notes/add.html` 表單頁面。
*   **輸入 (POST)**：表單欄位（心得內容、星級評分、標籤）。
*   **處理邏輯 (POST)**：建立新的 `Note` 與關聯標籤 (Tag)，並與該書籍綁定，存入 DB。
*   **輸出 (POST)**：建立成功後，重導向回該書籍詳情頁 `/books/<id>`。
*   **錯誤處理**：星級格式不符或內容為空時，回傳提示並重現表單。若指定的書籍 ID 不存在，回傳 404 頁面。

**依標籤探索書籍**
*   **輸入**：URL 變數 `<tag_name>`。
*   **處理邏輯**：用文字查詢該標籤，取得所有關聯的筆記及書籍紀錄。
*   **輸出**：渲染 `tags/index.html`。
*   **錯誤處理**：若查無此標籤的資料，回傳提示或顯示空狀態。

## 3. Jinja2 模板清單

所有檔案皆位於 `app/templates/` 之下：

*   `base.html`: 所有頁面共用的基底模板（包含導覽列 Navbar、Footer 以及全域共用資源的載入）。
*   `books/index.html`: 首頁與所有書籍列表，繼承自 `base.html`。
*   `books/search.html`: 搜尋結果呈現頁面，繼承自 `base.html`。
*   `books/add.html`: 新增書籍專用表單頁面，繼承自 `base.html`。
*   `books/detail.html`: 單一書籍詳細資訊、歷史筆記和評分列表，繼承自 `base.html`。
*   `notes/add.html`: 新增針對書籍的閱讀心得與評分表單，繼承自 `base.html`。
*   `tags/index.html`: 顯示經過特定標籤過濾後的結果列表版面，繼承自 `base.html`。
