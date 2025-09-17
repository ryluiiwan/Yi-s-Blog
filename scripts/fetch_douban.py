import feedparser
from datetime import datetime

# 你的豆瓣 RSS 链接
RSS_URL = "https://www.douban.com/feed/people/221855044/interests"

# Hugo about 页面路径（请按你的博客实际路径修改）
ABOUT_PATH = "content/zh/about.md"

def fetch_douban_feed(url):
    feed = feedparser.parse(url)
    items = []
    for entry in feed.entries[:10]:  # 最近 10 条
        title = entry.title
        link = entry.link
        # 格式化日期
        pub_date = datetime(*entry.published_parsed[:6]).strftime("%Y-%m-%d")
        items.append(f"- [{title}]({link})  ({pub_date})")
    return "\n".join(items)

def update_about_page():
    # 读取旧的 about.md
    with open(ABOUT_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # 生成豆瓣更新内容
    douban_md = fetch_douban_feed(RSS_URL)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 标记替换区域
    new_block = f"""
### 📚 最近的豆瓣动态（自动更新）
_Last update: {now}_

{douban_md}
"""

    # 如果之前有标记，替换；否则插入到最后
    if "<!-- douban start -->" in content and "<!-- douban end -->" in content:
        import re
        content = re.sub(
            r"<!-- douban start -->.*?<!-- douban end -->",
            f"<!-- douban start -->\n{new_block}\n<!-- douban end -->",
            content,
            flags=re.S,
        )
    else:
        content += f"\n\n<!-- douban start -->\n{new_block}\n<!-- douban end -->\n"

    # 写回文件
    with open(ABOUT_PATH, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    update_about_page()
