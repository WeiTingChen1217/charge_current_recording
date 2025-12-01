

# 充電環境監控系統  
**24小時自動拍照 + 高精度儀表 OCR + Excel 自動紀錄**

> 使用 PaddleOCR 2.8 + OpenCV 實作的工業級充電監控神器  
> 精準抓取溫度與濕度，永遠只認數字，永不崩潰！

## 功能亮點
- 每 5 秒自動拍照（可調整）
- 雙紅框精準鎖定溫度與濕度區域
- 100% 只輸出數字 + °C / %（絕對不會出現 B、G、O、S 等鬼東西）
- 自動寫入 Excel，支援長期監控與數據分析
- 防呆設計：模型抽風也不會 crash
- 乾淨的 Git 結構（不傳圖片、虛擬環境、Excel）

## 執行效果（實測截圖）


## 快速開始（30 秒部署）

# 1. Clone 專案
git clone https://github.com/WeiTingChen1217/charge_current_recording.git
cd charge_current_recording

# 2. 建立虛擬環境（推薦）
python -m venv venv
source venv/Scripts/activate      # Windows

# 3. 安裝依賴（一次就好）
pip install paddlepaddle==2.6.2
pip install paddleocr==2.8.1
pip install paddlex==3.3.10

# 4. 執行監控系統
python capture_ocr_to_excel.py
# 程式啟動後會開啟攝影機視窗，顯示兩個紅框：

# 請調整鏡頭讓紅框完全包住「溫度」與「濕度」數字
# 按 q 結束程式