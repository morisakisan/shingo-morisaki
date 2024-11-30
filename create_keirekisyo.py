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
                    
                </td>
            </tr>
            <tr>
                <td class="text-sm font-semibold px-4 py-2 border border-gray-300 w-1/5">
                    
                </td>
                <td class="px-4 py-2 border border-gray-300 w-4/5">
                    
                </td>
            </tr>
        </table>
        <h2 class="text-2xl font-bold mb-6">個人開発</h2>
        <table class="w-full border-collapse border border-gray-300 mb-6">
            <tr class="bg-gray-200">
                <td class="colspan-row text-center font-bold py-4 text-lg border border-gray-300" colspan="6">
                    
                </td>
            </tr>
            <tr>
                <td class="text-sm font-semibold px-4 py-2 border border-gray-300 w-1/5">
                    
                </td>
                <td class="px-4 py-2 border border-gray-300 w-4/5">
                    
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