from flask import Flask, request, Response
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = Flask(__name__)

@app.route('/SBPaymentResultReceiver/v1/data', methods=['GET', 'POST'])
def sb_payment_result_receiver():
    # リクエスト情報の取得
    body = request.get_data(as_text=True)
    content_type = request.headers.get('Content-Type')
    res_result = request.args.get('res_result')  # クエリパラメータから取得
    res_method = request.method

    # ログ出力（検証用）
    logging.info(f"Content-Type: {content_type}")
    logging.info(f"Body: {body}")
    logging.info(f"res_result: {res_result}")

    # HTMLとして表示（Shift_JISで返す）
    html_content = f"""
    <html>
      <head><meta charset="Shift_JIS"><title>SBペイメント検証</title></head>
      <body>
        <h2>決済結果を受信しました</h2>
        <p>{res_method}</p>
        <p><strong>res_result:</strong> {res_result}</p>
        <p><strong>Content-Type:</strong> {content_type}</p>
        <p><strong>Body:</strong> {body}</p>
      </body>
    </html>
    """

    # response = Response(html_content.encode('shift_jis'), content_type='text/html; charset=Shift_JIS')
    # response.status_code = 200
    # return response
    # レスポンス内容
    csv_content = 'OK,'

    # Shift_JISでエンコード
    encoded_content = csv_content.encode('shift_jis')

    # Flaskのレスポンスオブジェクトで返す
    response = Response(
        encoded_content,
        status=200,
        content_type='text/csv; charset=Shift_JIS'
    )
    return response

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
