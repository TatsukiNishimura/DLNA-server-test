# DLNA サーバ立ててみるプロジェクト

# 注意点

- twisted のエラー

  https://github.com/opacam/Cohen3/issues/45

  バージョン指定すれば OK

  requirements.txt に記述済み

# サーバーを立てる

```
cohen3 --plugin=backend:FSStore,content:1654
```

# lint

- black & isort

```
make fmt
```

- check error

```
flake8 src
```
