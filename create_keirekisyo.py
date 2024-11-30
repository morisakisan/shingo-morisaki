import json
from jinja2 import Template

# Jinja2テンプレートを定義
template = Template("""
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>スキルシート</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 text-gray-800">
    <main class="max-w-4xl mx-auto my-10 p-6 bg-white rounded-lg shadow-md">
        <h1 class="text-3xl font-bold text-center mb-6">スキルシート</h1>
        <h2 class="text-2xl font-bold mb-6">プロフィール</h2>
        <table class="w-full border-collapse border border-gray-300 mb-6">
            <tr class="bg-gray-200">
                <td class="colspan-row text-center font-bold py-4 text-lg border border-gray-300" colspan="6">
                    お名前
                </td>
            </tr>
            <tr>
                <td class="text-sm font-semibold px-4 py-2 border border-gray-300 w-1/5">性別</td>
                <td class="px-4 py-2 border border-gray-300 w-4/5">男</td>
            </tr>
            <tr>
                <td class="text-sm font-semibold px-4 py-2 border border-gray-300 w-1/5">生年月日</td>
                <td class="px-4 py-2 border border-gray-300 w-4/5">？</td>
            </tr>
            <tr>
                <td class="text-sm font-semibold px-4 py-2 border border-gray-300 w-1/5">学歴</td>
                <td class="px-4 py-2 border border-gray-300 w-4/5">？</td>
            </tr>
        </table>
        <h2 class="text-2xl font-bold mb-6">個人開発</h2>
        <table class="w-full border-collapse border border-gray-300 mb-6">
            <tr class="bg-gray-200">
                <td class="colspan-row text-center font-bold py-4 text-lg border border-gray-300" colspan="6">
                    クイズのSNS
                </td>
            </tr>
            <tr>
                <td class="text-sm font-semibold px-4 py-2 border border-gray-300 w-1/5">
                    使用言語
                </td>
                <td class="px-4 py-2 border border-gray-300 w-4/5">
                    Dart
                </td>
            </tr>
            <tr>
                <td class="text-sm font-semibold px-4 py-2 border border-gray-300 w-1/5">
                    リンク
                </td>
                <td class="px-4 py-2 border border-gray-300 w-4/5">
                    <ul class="list-disc list-inside text-gray-700">
                        <li>
                            <a href="https://play.google.com/store/apps/details?id=com.shingo.share_quiz&hl=ja-JP" 
                            target="_blank" 
                            class="text-blue-500 hover:underline">
                                Google Play Store
                            </a>
                        </li>
                        <li>
                            <a href="https://github.com/morisakisan/share_quiz" 
                            target="_blank" 
                            class="text-blue-500 hover:underline">
                                GitHub Repository
                            </a>
                        </li>
                    </ul>
                </td>
            </tr>
            <tr>
                <td class="text-sm font-semibold px-4 py-2 border border-gray-300 w-1/5">
                    使用ツール
                </td>
                <td class="px-4 py-2 border border-gray-300 w-4/5">
                    Android Studio, Firebase, Git, GitHub, GitHubActions
                </td>
            </tr>
            <tr>
                <td class="text-sm font-semibold px-4 py-2 border border-gray-300 w-1/5">
                    使用ライブラリー
                </td>
                <td class="px-4 py-2 border border-gray-300 w-4/5">
                    hooks riverpod, flutter settings ui, rxdart, freezed
                </td>
            </tr>
            <tr>
                <td class="text-sm font-semibold px-4 py-2 border border-gray-300 w-1/5">
                    説明
                </td>
                <td class="px-4 py-2 border border-gray-300 w-4/5">
                    Flutterを学習したのでポートフォリオとして作ってみました。ログインしてクイズを投稿するSNSのような側面を持つアプリケーションです。クリーンアーキテクチャで設計を行いました。現状の機能としては、ログイン機能、ログアウト機能、退会機能、クイズ一覧表示機能、クイズ投稿機能、クイズ解答機能、クイズにいいねを行う機能、クイズをsnsなどで共有する機能がございます。また、GitHubActionsでのCI/CDを導入しました。PR作成時にはビルドとFirebaseへのデプロイを行います。また、masterへのmergeの際には、Google Playの内部共有にアプリケーションをデプロイするワークフローを作成しました。現状Android版しか出していませんが、Flutterで開発しているので今後はios版、web版をリリースしたいです。またコメント機能、検索機能などの機能追加やデザインの修正も検討中です
                </td>
            </tr>
        </table>
        <h2 class="text-2xl font-bold mb-6">経歴書</h2>
        {% for project in projects %}
        <table class="w-full border-collapse border border-gray-300 mb-6">
            <tr class="bg-gray-200">
                <td class="colspan-row text-center font-bold py-4 text-lg border border-gray-300" colspan="6">
                    {{ project.title }}
                </td>
            </tr>
            {% for detail in project.details %}
            <tr>
                <td class="text-sm font-semibold px-4 py-2 border border-gray-300 w-1/5">
                    {{ detail.label }}
                </td>
                <td class="px-4 py-2 border border-gray-300 w-4/5">
                    {{ detail.value }}
                </td>
            </tr>
            {% endfor %}
        </table>
        {% endfor %}
    </main>
</body>
</html>
""")

# JSONファイルを読み込む
with open("keirekisyo.json", "r", encoding="utf-8") as file:
    projects = json.load(file)

# HTML生成
html_output = template.render(projects=projects)

# HTMLを保存
with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(html_output)

print("HTMLファイルを生成しました: index.html")