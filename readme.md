//建立虛擬環境，減少版本依賴衝突
python -m venv venv
source venv/Scripts/activate      # Windows

pip install paddlepaddle==2.6.2
pip install paddleocr==2.8.1
pip install paddlex==3.3.10

