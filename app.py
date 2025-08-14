import sqlite3
import click
from flask import Flask, jsonify, render_template, request, g, current_app
from flask.cli import with_appcontext
import random

# --- アプリケーション設定 ---
DATABASE = 'typography.db' # データベースファイル名

app = Flask(__name__)
app.config.from_object(__name__) # アプリケーションの設定を読み込む

# --- データベース関連の関数 ---

def get_db():
    """リクエストごとにデータベース接続を確立し、再利用する"""
    if 'db' not in g:
        g.db = sqlite3.connect(
            app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # 辞書形式で結果を取得できるようにする
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(e=None):
    """リクエスト終了時にデータベース接続を閉じる"""
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    """データベーススキーマに基づいてテーブルを初期化する"""
    db = get_db()
    with current_app.open_resource('schema.sql', mode='r', encoding='utf-8') as f:
        db.cursor().executescript(f.read())
    db.commit()

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Flaskコマンドとしてデータベース初期化を登録"""
    init_db()
    click.echo('Initialized the database.')

app.cli.add_command(init_db_command)

# --- APIエンドポイント ---

@app.route('/')
def index():
    """メインページをレンダリングする"""
    return render_template('index.html')

@app.route('/api/settings', methods=['GET'])
def get_all_settings():
    """保存されているすべての設定を取得する"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM typography_settings ORDER BY created_at DESC')
    settings = cursor.fetchall()
    # sqlite3.Rowオブジェクトを辞書のリストに変換
    return jsonify([dict(row) for row in settings])

@app.route('/api/settings', methods=['POST'])
def add_setting():
    """新しいタイポグラフィ設定をデータベースに保存する"""
    data = request.json
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute(
            '''
            INSERT INTO typography_settings (
                name, text_content, font_family, font_size, font_color,
                background_color, text_align, shadow_enabled, shadow_color,
                shadow_blur, shadow_offset_x, shadow_offset_y, stroke_enabled,
                stroke_color, stroke_width
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''',
            (
                data['name'], data['textContent'], data['fontFamily'], data['fontSize'],
                data['fontColor'], data['backgroundColor'], data['textAlign'],
                data['shadowEnabled'], data['shadowColor'], data['shadowBlur'],
                data['shadowOffsetX'], data['shadowOffsetY'], data['strokeEnabled'],
                data['strokeColor'], data['strokeWidth']
            )
        )
        db.commit()
        # 挿入されたデータのIDを取得
        inserted_id = cursor.lastrowid
        # 挿入されたデータを取得して返す
        cursor.execute('SELECT * FROM typography_settings WHERE id = ?', (inserted_id,))
        new_setting = cursor.fetchone()
        return jsonify(dict(new_setting)), 201
    except sqlite3.Error as e:
        db.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/api/settings/random', methods=['GET'])
def get_random_setting():
    """保存されている設定の中からランダムに1つを取得する"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM typography_settings')
    settings = cursor.fetchall()
    if not settings:
        return jsonify({'error': 'No settings saved yet.'}), 404
    
    random_setting = random.choice(settings)
    return jsonify(dict(random_setting))

# --- アプリケーション実行 ---
if __name__ == '__main__':
    app.run(debug=True)
