# Finnlove 挂件合集

天气 · 时钟 · 壁纸 — 一站式的小挂件库，适合嵌入 Notion、个人主页或任何网页。

> 从原来的 17 个分散仓库合并而来，保留了 7 个最有价值的实现。

## 预览

打开 `index.html` 即可看到所有挂件的卡片式预览。

## 挂件清单

### 1. 时钟 + 天气卡片 (`clock-weather/`)
- **特点**：手写 JS 实现 12 小时时钟，带日期、时段问候语
- **风格**：薄荷绿卡片 + 百度动态 GIF 背景
- **适合**：Notion 页面、个人主页
- **依赖**：Google Fonts (Sofia, Lobster, Roboto)

### 2. 必应三合一 (`bing-trinity/`)
- **特点**：必应每日壁纸 + timeanddate.com 时钟 + 和风天气
- **风格**：全宽大图，白色文字叠加
- **适合**：大屏展示、桌面小组件
- **依赖**：Bing Wallpaper API, timeanddate.com, QWeather

### 3. 必应三合一·紧凑版 (`bing-compact/`)
- **特点**：300px 宽的迷你版，使用 `api.dujin.org` 代理 Bing 图片
- **风格**：小尺寸卡片
- **适合**：Notion 侧边栏、小窗口嵌入
- **依赖**：同上

### 4. 动画天气图标 (`animated-icons/`)
- **特点**：Climacons Animated 动态天气图标，candy 主题
- **风格**：清新渐变，3 天预报
- **适合**：需要动态效果的场景
- **依赖**：weatherwidget.io

### 5. 背景图 + 动画图标 (`bg-image-icons/`)
- **特点**：GIF 背景图 + 白色文字天气
- **风格**：视觉冲击力强
- **适合**：装饰性展示
- **依赖**：weatherwidget.io, 百度图片 CDN

### 6. 透明背景天气 (`transparent/`)
- **特点**：Sharp Weather，完全透明背景
- **风格**：水平布局，可融入任何底色
- **适合**：嵌入已有设计的页面
- **依赖**：Sharp Weather (weatherwidget.org)

### 7. 简约滚动天气 (`simple-scroll/`)
- **特点**：world-weather.info 滚动文字，最轻量
- **风格**：纯文字，无图片依赖
- **适合**：极简风格页面
- **依赖**：world-weather.info

## 使用方式

### 嵌入 Notion
1. 将对应 `index.html` 部署到 GitHub Pages
2. 在 Notion 中使用 `/embed` 块，粘贴 GitHub Pages URL

### 嵌入个人主页
直接用 `<iframe>` 引用：
```html
<iframe src="https://your-username.github.io/bg-1weather/clock-weather/index.html" width="100%" height="100" frameborder="0"></iframe>
```

### 本地预览
```bash
# 在项目目录下启动本地服务器
python -m http.server 8080
# 浏览器打开 http://localhost:8080
```

## 天气 API 说明

| 挂件 | 天气服务 | 需要 API Key |
|---|---|---|
| clock-weather | world-weather.info | ❌ (userid 嵌入) |
| bing-trinity | QWeather (和风天气) | ✅ (已内置) |
| bing-compact | QWeather (和风天气) | ✅ (已内置) |
| animated-icons | weatherwidget.io | ❌ (免费) |
| bg-image-icons | weatherwidget.io | ❌ (免费) |
| transparent | Sharp Weather | ❌ (免费) |
| simple-scroll | world-weather.info | ❌ (userid 嵌入) |

## 文件结构

```
bg-1weather/
├── index.html              # 主预览页（卡片式展示所有挂件）
├── clock-weather/          # 时钟+天气卡片（原创 JS）
│   └── index.html
├── bing-trinity/           # 必应三合一（大屏）
│   └── index.html
├── bing-compact/           # 必应三合一（紧凑）
│   └── index.html
├── animated-icons/         # 动画天气图标
│   └── index.html
├── bg-image-icons/         # 背景图+动画图标
│   └── index.html
├── transparent/            # 透明背景天气
│   └── index.html
├── simple-scroll/          # 简约滚动天气
│   └── index.html
└── README.md
```

## 原始仓库对照

| 合并后的挂件 | 原始仓库 | 状态 |
|---|---|---|
| clock-weather | `bg-1weather` / `clock-test` | ✅ 保留（clock-test 为重复） |
| bing-trinity | `biyingclock` | ✅ 保留 |
| bing-compact | `biyingtimew` | ✅ 保留 |
| animated-icons | `guajiantianqi` | ✅ 保留 |
| bg-image-icons | `tianqiguajian` | ✅ 保留 |
| transparent | `transforweather` | ✅ 保留 |
| simple-scroll | `weather2` | ✅ 保留 |

**已被合并的重复仓库**（建议 Archive）：
- `clock-test` = bg-1weather 的完全复制
- `HDtime` = HDclock 的完全复制
- `timehd` = HDclock 仅改了背景色
- `-` = transforweather 的复制
- `tianqigj1` = tianqiguajian 的复制（且文件无扩展名）
- `BG-weather` = 空仓库
- `weather` = world-weather.info 简单嵌入（功能被 simple-scroll 覆盖）
- `wether-1` = 同上
- `biyingtime` = 未完成的教程版
- `biyingtimew` 的大屏版（功能被 bing-trinity 覆盖）
- `HDclock` = Indify.co 嵌入（第三方依赖重，不推荐）

---

*Originally from Finnlove's GitHub repositories. Merged and organized.*
