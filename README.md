# DLNA サーバ立ててみるプロジェクト

# Version

Python 3.8.6 で動作確認済み

Python3.10 は ×

# 使い方

## 動画ファイルの用意

動画ファイルを入れたフォルダを用意する（名前はなんでもいい）

## DLNA サーバーを立てる

```
cohen3 --plugin=backend:FSStore,content:(↑で用意したフォルダ名)
```

ex: フォルダ名が 1654 なら

```
cohen3 --plugin=backend:FSStore,content:1654
```

## 接続

localhost:8080 にサーバが建てられるので、

適当な DLNA Client で接続する

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
