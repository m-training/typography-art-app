# タイポグラフィ・アート生成アプリ

ユーザーが入力したテキストから、ランダムなスタイルを適用して視覚的に面白いタイポグラフィ・アートを生成するWebアプリケーションです。生成したアートの設定は保存し、後から呼び出すことができます。

## 必要なもの

- Python 3.x
- Flask

Flaskがインストールされていない場合は、以下のコマンドでインストールしてください。

```bash
pip install Flask
```

## セットアップと実行手順

### ファイルの配置

以下のファイルを次のような構造で保存してください。

```Plaintext
/your_project_folder
├── app.py
├── schema.sql
├── README.md
└── /templates
    └── index.html
```

### データベースの初期化

ターミナル（コマンドプロンプト）を開き、`your_project_folder` に移動して、以下のコマンドを実行します。これにより、`typography.db` というデータベースファイルとテーブルが作成されます。

**macOS / Linux:**

```bash
export FLASK_APP=app.py
flask init-db
```

**Windows:**

```bash
set FLASK_APP=app.py
flask init-db
```

実行後、「Initialized the database.」と表示されれば成功です。

### アプリケーションの起動

以下のコマンドでFlask開発サーバーを起動します。

```bash
flask run
```

### アクセス

Webブラウザを開き、次のURLにアクセスしてください。
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## フォントの追加・変更方法

新しいWebフォントを追加したり、既存のフォントを変更したりするのは簡単です。

### Google Fontsでフォントを選択

[Google Fonts](https://fonts.google.com/) にアクセスし、使いたいフォントを探します。

### `<link>` タグの取得

使いたいフォントを選択し、`<link>` タグをコピーします。例えば、「Noto Sans JP」と「RocknRoll One」を追加する場合は以下のようになります。

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700&family=RocknRoll+One&display=swap" rel="stylesheet">
```

### index.html の編集

`templates/index.html` ファイルを開き、`<head>` セクションにある既存のGoogle Fontsの `<link>` タグを、新しくコピーしたものに置き換えます。

### JavaScriptのフォントリストを更新

同じく `index.html` ファイル内の `<script>` タグにある `webFonts` 配列を編集します。CSSで指定するフォント名を文字列として追加してください。

```javascript
// 利用可能なWebフォントのリスト
const webFonts = [
    'serif',
    'sans-serif',
    'monospace',
    'cursive',
    'fantasy',
    'Orbitron',
    'Press Start 2P',
    // ここに新しいフォント名を追加
    'Noto Sans JP',
    'RocknRoll One'
];
```

ファイルを保存すれば、アプリケーションに新しいフォントが反映されます。
