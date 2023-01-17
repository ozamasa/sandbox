import time
from datetime import datetime
from napalm import get_network_driver
from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference


def func():
    # 「ios」を指定してドライバを取得
    driver = get_network_driver('ios')
    # ルータの認証情報を設定
    device = driver(hostname='192.168.100.112',
                    username='user0',
                    password='pass',
                    optional_args={'secret': 'epass', 'inline_transfer': True}
                    )
    device.open()   # ルータに接続

    wb = Workbook()   # Workbookオブジェクトを取得
    ws = wb.active  # アクティブワークシートを取得

    ws.append(['日時', '受信オクテット', '送信オクテット'])

    counter = 20    # 繰り返し回数を設定
    for i in range(counter):
        # インターフェースカウンターを取得
        interfaces_counters = device.get_interfaces_counters()
        ge = interfaces_counters['GigabitEthernet0/0']
        row = []
        row.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # 取得日時
        row.append(ge['rx_octets'])  # 受信オクテットカウンタ
        row.append(ge['tx_octets'])  # 送信オクテットカウンタ
        ws.append(row)  # ワークシートに出力
        time.sleep(5)   # 5秒待って、処理を繰り返す

    device.close()      # ルータとの接続を閉じる

    chart = LineChart()   # 折れ線グラフオブジェクトを取得

    # グラフのデータ範囲を設定
    values = Reference(ws, min_col=2, min_row=1, max_col=3, max_row=counter+1)
    chart.add_data(values, titles_from_data=True)

    # 横軸の項目範囲を設定
    cats = Reference(ws, min_col=1, min_row=2, max_col=1, max_row=counter+1)
    chart.set_categories(cats)

    ws.add_chart(chart, 'E1')   # ワークシートにグラフを出力

    wb.save("interfaces_counters.xlsx")   # ワークブックを保存


if __name__ == "__main__":                                      # ... 8
    func()
