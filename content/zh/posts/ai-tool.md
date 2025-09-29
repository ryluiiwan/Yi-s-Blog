---
title: "[Ai MiniTools]一个简单的头像生成器"
slug: ai-avatar-generator
date: "2025-09-29T21:16:31+08:00"
draft: false
lastmod: "2025-09-29T21:16:31+08:00"
tags: ["Ai"]
categories: ["learning"]
authors:
  - "ryluiiwan"
---

1 小时快速构建自己的 AI 小工具，此项目参考[Andy 四海为家](https://andyroamer.com/articles/ai-code-claude-website)的教程，使用 Next.js 框架、最后 Vercel 部署上线，全部使用 [Claude Sonnet4](https://claude.ai/) 完成，不用写一句代码。

## 🎇1. 主要功能：

用户输入关键词并选择想要的图片风格(卡通动漫、Q 版头像、赛博朋克、蒸汽波、像素风、Emoji)调用 SD3 的 API 来生成头像，用户可以选择两种图片格式来下载生成的头像。

👉 快来试一下：[AI 头像生成器](https://avatar-five-alpha.vercel.app/)

📦 仓库地址：[Github](https://github.com/ryluiiwan/avatar)

## 📄2. 项目结构

```
avatar/
├── app/
│ ├── page.tsx # 前端页面
│ ├── api/
│ │ └── avatar/
│ │ └── route.ts # 后端 API
│ ├── globals.css # 全局样式
│ └── layout.tsx # 布局文件
├── .env.local # 环境变量
├── package.json # 依赖配置
├── tailwind.config.js # Tailwind 配置
├── tsconfig.json # TypeScript 配置
└── next.config.js # Next.js 配置
```

## 🚀3. 快速开始

前置环境：

- Node.js 18.18 或以上版本
- MacOs / Windows / Linux

### 安装 Next.js 框架

首先安装打开[Next.js](https://nextjs.org/docs/app/getting-started/installation)官网下载框架,在终端(Terminal)运行以下命令：

```
npx create-next-app@latest
```

_BUG_: 卡在第一步，需要检查一下自己的代理的端口号, 然后在 VS code 的终端输入下面的命令,注意将 10808 替换为自己的代理端口号：

![端口号](/images/Avatar/01.png)

```
$env:http_proxy = "http://127.0.0.1:10808"
回车后再输入
$env:http_proxy = "https://127.0.0.1:10808"
```

![下载成功提示](/images/Avatar/02.png)

下载成功后，进入该项目，并输入如下命令，启动该项目,就可以在本地来调试访问了：

```
npm run dev
```

### Claude Code 生成代码，本地调试

Prompt 指令，仅供参考，生成的代码需要不断地让 Claude 来 debug。

```
我想制作一个AI头像生成器 调用Stable diffusion3 接口来生成512px×512px的社交媒体头像 用户输入内容 输出头像 主要框架是Next.js 是app路由 tailwindcss typescript语法 我现在在本地windows电脑进行调试 之后会部署到vercel上

前端页面可以输入内容框、选择对应的风格（证件照 卡通动漫 Q版头像 赛博朋克 蒸汽波 像素风 emoji风格）你需要提前写好各个风格的promote指令和用户输入内容构建一个完整的promote指令、生成之后可以看到对应图片

我的前端页面路径是avatar\app\page.tsx 后端页面路径是avatar\app\api\avatar\route.ts

后端页面调用SD3的接口，需要遵循SD3的官方接口规范 接口规范如下 import fs from "node:fs"; import axios from "axios"; import FormData from "form-data"; const payload = { prompt: "Lighthouse on a cliff overlooking the ocean", output_format: "webp" }; const response = await axios.postForm( https://api.stability.ai/v2beta/stable-image/generate/ultra, axios.toFormData(payload, new FormData()), { validateStatus: undefined, responseType: "arraybuffer", headers: { Authorization: Bearer sk-MYAPIKEY, Accept: "image/*" }, }, ); if(response.status === 200) { fs.writeFileSync("./lighthouse.webp", Buffer.from(response.data)); } else { throw new Error(${response.status}: ${response.data.toString()}); } 现在给我完整代码
```

Claude 生成的代码，需要按照 `📄2. 项目结构`中的结构复制到对应的文件中。
![Claude生成代码](/images/Avatar/03.png)

环境变量文件需要自己新建一个，里面是 SD3 的 API key，注册[SD3](https://platform.stability.ai/account/keys)之后，每个账户会有一定的免费额度来使用，复制这个密钥，在`.env.local`文件中输入：

```
STABILITY_API_KEY=Your Key

```

碎碎念：中间的 debug 步骤省略，太乱了，脑子都忘记是怎么解决了，把遇到的日志文件全部粘贴给 Claude，它会帮你来更新最新版本的 code，反正就是遇到问题解决问题，全部让 AI 来解决，不过改到后面真的蛮乱的代码改了小 10 个 version，所以版本控制还是挺重要的，另外感觉还是要去学一下 Next.js，懂点儿代码改起来都没那么费劲。

### Vercel 部署上线

在使用 Vercel 部署上线前，需要将本地的代码 push 到 github 仓库，在 VS code 里面全部可以傻瓜式完成，都不用`git add .`、`git commit -m ""`、`git push`。

注册 [Vercel](https://vercel.com/)，我选择的是使用 github 登录，导入自己仓库的项目，Vercel 会自动开始部署，并分配一个免费的域名。

![Vercel部署](/images/Avatar/04.png)

注意：因为 API Key 的隐私性问题，这个环境需要在 Vercel 项目设置那里更改一下，将原来环境变量里面的 API keyu 复制到项目环境那里，如下图所示：

![Vercel部署](/images/Avatar/05.png)

后续可以购买域名，添加 DNS 解析，懒得折腾了，不过真的现在 AI 的发展很迅速，制作一个产品的门槛与成本已经大大降低，像我对前端只懂点 HTML 和 CSS 的人来说能这么快就造个小玩具出来，感觉快被时代淘汰了哈哈哈哈。

---END---
