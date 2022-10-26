# DLNA サーバ立ててみるプロジェクト

## 使い方

## 動画ファイルの用意

動画ファイルを入れたフォルダを用意する（名前はなんでもいい）

## DLNA サーバーを立てる

```
cohen3 --plugin=backend:FSStore,content:(↑で用意したフォルダ名)
```

ex: フォルダ名が media なら

```
cohen3 --plugin=backend:FSStore,content:media
```

## 接続

localhost:8080 にサーバが建てられるので、

適当な DLNA Client で接続する

# ファイル操作サーバー

FastAPI で作成

## 使い方

1. ファイル操作のためのテストデータを作成

```
python make_test_data.py
```

2. サーバを起動

```
cd src && uvicorn main:app --reload
```

3. localhost:8000 にアクセス

## API

- localhost:8000/docs に swagger が自動生成されるので参照

# lint

- black & isort

```
make fmt
```

- check error

```
flake8 src
```

# 注意点

- twisted のエラー

  https://github.com/opacam/Cohen3/issues/45

  requirements.txt に記述済み
