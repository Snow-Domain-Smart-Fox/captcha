# captcha
基于 ppllocr 的验证码 OCR 识别服务

# 鸣谢
感谢 [ppllocr](https://github.com/gitpetyr/ppllocr) 提供的技术支持。

# 一键拉取并启动
```bash
git clone https://github.com/Snow-Domain-Smart-Fox/captcha.git
cd captcha
pip install flask ppllocr
python server.py
```

# 指定端口
```bash
git clone https://github.com/Snow-Domain-Smart-Fox/captcha.git
cd captcha
pip install flask ppllocr
python server.py --port [PORT]
```

# captcha 项目 OCR 接口使用说明
基于 GitHub 项目：https://github.com/Snow-Domain-Smart-Fox/captcha/

## 1. 启动服务
```bash
python server.py --port [PORT]
```

## 2. 接口信息
- 请求地址：`http://你的IP:端口/ocr`
- 请求方式：POST
- 数据格式：JSON

## 3. 请求参数
```json
{
  "image": "图片的base64编码字符串（可带data:image/xxx;base64,前缀）"
}
```

## 4. 响应结果
- 成功：`{"code":0,"data":"识别内容","msg":"success"}`
- 失败：`{"code":-1,"msg":"错误原因"}`

## 5. 依赖安装
```bash
pip install flask ppllocr
```
