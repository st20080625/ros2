# ROS2 Tutorial Repository

このリポジトリは、**ROS2の基本プログラム、micro-ROS、Gazeboシミュレータ、およびDockerコンテナ環境**を一つにまとめた学習用リポジトリです。

## 概要
本リポジトリは、ROS2の開発環境をDockerでパッケージ化しており、OSを問わず（Windows/Linux）スムーズに開発を始めることができます。

## 学習の進め方
まずはリポジトリに含まれている解説資料（PDF）を確認してください。

👉 **[ros2_tutorial.pdf](./ros2_tutorial.pdf)**

このドキュメントでは以下の内容を詳しく解説しています：
* **ROS2の基本概念**: ノード、トピック、サービス通信の仕組み
* **環境構築**: Dockerを用いたコンテナ環境の立ち上げ手順
* **実践演習**: C++を用いたPublisher/Subscriberの実装方法
* **シミュレーション**: Gazeboを用いたクローラロボットの操作
* **数学的背景**: tf（座標系管理）に必要なクォータニオンや回転の知識

資料を読みながら実際にROS2に触れ、各プログラムの挙動や通信の仕組みに慣れてください。

## クイックスタート
Docker Desktop（またはDocker Compose）がインストールされている環境であれば、以下のコマンドで環境を起動できます。

```bash
# リポジトリのクローン
git clone https://github.com/rudolfkalman/ros2.git
cd ros2

# コンテナビルドと起動
sudo docker compose up -d ros2

# ROS2コンテナに入る
sudo docker exec -it ros2-jazzy /bin/bash
# または
./scripts/enter_ros.sh