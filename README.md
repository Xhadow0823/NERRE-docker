# Before start this service
1. clone this repo
2. cd to this dir
3. prepare your open ai api key

# Start this service
1. Method1 - run with docker
  1. build this image
    `sudo docker build --tag NERRE .`
  2. then run with docker
    `sudo docker run -it --rm -p 5000:5000 -e OPENAI_API_KEY="xxxxx" --name my-nerre NERRE`
2. Method2 - build & run with docker-compose
  `echo OPENAI_API_KEY=xxxxx > .env && sudo docker compose up`

> Please replace all xxxxx with your open ai api key.

# How to use
- **實體關係提取工具** -- by TripleC
  - 將欲要處理抽取實體關係之文章放到欄位內
  抑或是直接將.txt檔經由選擇檔案按鈕做選取並導入
  - 按下開始提取按鈕，會呈現處理中字樣，請耐心等待
  - 完成會呈現處理完成字樣，並出現處理結果
  結果包括實體與關係.csv檔形式
  - 可點擊下載進行實體.csv檔與關係.csv檔下載
      - 不能使用excel開啟實體.csv檔與關係.csv檔，會呈現亂碼
      若使用記事本開就會正常呈現實體與關係
  - 歷史結果是會統整出之前所提取的紀錄，可點擊進行下載
- Example
  - ![example1](example1.gif)

## misc
+ http://{url_of_your_location}:5000
