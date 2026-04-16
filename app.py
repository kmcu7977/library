from flask import Flask, render_template, request, jsonify
import sqlite3
import json
import os

app = Flask(__name__)

# ▼▼▼ 여기를 수정했습니다 (경로 문제 방지) ▼▼▼
# 현재 app.py가 있는 폴더의 위치를 찾음
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 그 폴더 안에 library.db를 만듦
DB_FILE = os.path.join(BASE_DIR, 'library.db')
# ▲▲▲ 수정 끝 ▲▲▲

# DB 초기화 함수 (서버 켤 때 테이블 없으면 자동 생성)
def init_db():
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        # id=1인 행 하나에 모든 JSON 데이터를 텍스트로 때려박는 단순한 구조입니다.
        c.execute('''CREATE TABLE IF NOT EXISTS checklist
                     (id INTEGER PRIMARY KEY, content TEXT)''')
        # 초기 빈 데이터 생성
        c.execute('INSERT INTO checklist (id, content) VALUES (1, "[]")')
        conn.commit()
        conn.close()
        print("DB 초기화 완료")

# 메인 페이지 접속
@app.route('/')
def index():
    return render_template('index.html')

# 데이터 불러오기 (GET)
@app.route('/api/load', methods=['GET'])
def load_data():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT content FROM checklist WHERE id=1')
    row = c.fetchone()
    conn.close()
    
    if row:
        return jsonify(json.loads(row[0])) # DB에 있는 텍스트를 JSON으로 변환해서 줌
    else:
        return jsonify([])

# 데이터 저장하기 (POST)
@app.route('/api/save', methods=['POST'])
def save_data():
    data = request.json # 프론트에서 보낸 JSON 데이터
    json_str = json.dumps(data) # 텍스트로 변환
    
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('UPDATE checklist SET content = ? WHERE id=1', (json_str,))
    conn.commit()
    conn.close()
    
    return jsonify({"status": "success"})

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)