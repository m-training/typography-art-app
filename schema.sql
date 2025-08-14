-- データベースの既存のテーブルを削除してクリーンな状態にする
DROP TABLE IF EXISTS typography_settings;

-- タイポグラフィ設定を保存するためのテーブルを作成
CREATE TABLE typography_settings (
  id INTEGER PRIMARY KEY AUTOINCREMENT, -- ユニークなID
  name TEXT NOT NULL, -- ユーザーが設定につける名前
  text_content TEXT NOT NULL, -- アートの元になるテキスト
  font_family TEXT NOT NULL, -- フォント名
  font_size INTEGER NOT NULL, -- フォントサイズ
  font_color TEXT NOT NULL, -- 文字色 (例: '#RRGGBB')
  background_color TEXT NOT NULL, -- 背景色
  text_align TEXT NOT NULL, -- テキストの配置 ('left', 'center', 'right')
  shadow_enabled INTEGER NOT NULL, -- 影の有無 (0: false, 1: true)
  shadow_color TEXT NOT NULL, -- 影の色
  shadow_blur INTEGER NOT NULL, -- 影のぼかし具合
  shadow_offset_x INTEGER NOT NULL, -- 影のX軸オフセット
  shadow_offset_y INTEGER NOT NULL, -- 影のY軸オフセット
  stroke_enabled INTEGER NOT NULL, -- アウトラインの有無 (0: false, 1: true)
  stroke_color TEXT NOT NULL, -- アウトラインの色
  stroke_width INTEGER NOT NULL, -- アウトラインの太さ
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP -- 作成日時
);
