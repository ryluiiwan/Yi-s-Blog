---
title: "Hugo + Cloudflare部署个人博客"
date: 2024-12-07T12:11:08+08:00
draft: false
lastmod: 2024-12-07T12:11:08+08:00
tags: ["Blog", "hugo"]
categories: ["tools"]
authors:
  - "ryluiiwan"
---

之前尝试过很多次自己搭建个人博客，总是无疾而终，没有耐性、三心二意应该是我最大的缺点。最近裸辞休养生息还是觉得要做点什么，还是来完成我 22 年还是 23 年就想做的事情，创建一个个人博客。很多事情对我来说，我很难坚持从头到尾做完，没有强烈的热情，总是想一出是一出。

这次也想看看我能不能把这件事，从头到尾做完，并不断完善。准备开始折腾，顺便捡起本科的渣渣编程基础。有天在搜索 Hugo 的时候突然看到了[pseudoyu](https://www.pseudoyu.com/zh/2022/05/29/deploy_your_blog_using_hugo_and_github_action/)大佬做的博客，故按照他的教程来搞一个静态博客，做一个自己的网络自留地。

## 📍 安装 Hugo

系统：`Windows10`

### 下载 Hugo

- 打开 [Hugo 官方 GitHub Release 页面](https://github.com/gohugoio/hugo/releases)。
- 找到最新版本，下载适合 Windows 的二进制文件：
  - 如果你的 Windows 是 64 位，选择 `hugo_extended_x.y.z_Windows-64bit.zip`（`x.y.z` 是版本号）
  - 如果不需要扩展功能（如 SCSS 支持），也可以选择普通的 `hugo_x.y.z_Windows-64bit.zip`

### 解压文件

- 将下载的 ZIP 文件解压到一个文件夹，例如 `D:\hugo`
- 你应该能在`bin`文件夹中看到一个 `hugo.exe` 文件

### 配置环境变量

- **打开系统环境变量设置：**
  - 在搜索栏中输入 **“环境变量”**，选择 **“编辑系统环境变量”**
  - 点击 **“环境变量”** 按钮
- **添加 Hugo 到 PATH：**
  - 在 **系统变量** 下找到 `Path`，选中后点击 **编辑**
  - 点击 **新建**，输入 Hugo 的路径，例如：`D:\hugo\bin`
  - 点击 **确定**，保存所有设置

### 验证安装

- 打开命令提示符（`cmd`），输入以下命令：

```shell
hugo version
```

- 如果安装成功，你会看到类似下面的输出：

```
hugo v0.128.2-de36c1a95d28595d8243fd8b891665b069ed0850+extended windows/amd64 BuildDate=2024-07-04T08:13:25Z VendorInfo=gohugoio
```

### 初始化站点

- 创建新项目

```shell
hugo new site ryluiiwan.com
```

- 进入项目目录

```shell
cd ryluiiwan.com
```

### 初始化 git 仓库

创建好的项目是没有被 Git 管理的，所以需要初始化 Git 仓库

- 初始化一个新的 git 仓库

```shell
git init
```

- 将**工作区中所有的更改**添加到暂存区（Staging Area）

```shell
git add .
```

- 提交你在暂存区中的更改到本地仓库，并为这个提交添加一条描述信息

```shell
git commit -m "first commit"
```

- **重命名当前分支**为 `main`,

```shell
git branch -M main
```

- 将远程仓库关联到本地仓库

```shell
git remote add origin git@github.com:ryluiiwan/ryluiiwan.com.git
```

### 引用主题

- 下载`den`主题：克隆了[pseudoyu](https://github.com/pseudoyu/hugo-theme-den)的博客项目

```shell
git submodule add https://github.com/pseudoyu/hugo-theme-den themes/hugo-theme-den
```

- 初始化

```shell
git submodule update --init --recursive
```

- 开始使用主题时将其 exampleSite/ 目录下的文件复制到站点目录下，在此基础上进行调整配置。

```shell
cp -rf themes/hugo-theme-den/exampleSite/* ./
```

- 然后修改 Hugo 的配置(`hugo.toml`)

- 修改后，在本地启动服务，可以访问 `http://localhost:1313/` 来查看网站

```shell
hugo server
```

## 📍 发布博客工作流程

- 创建新的博客文件

新创建的文章默认会放在`content`目录下，文章的头信息可以修改`archetypes/default.md`这个模板。

我的文章模板是：

```markdown
---
title: '{{ replace .File.ContentBaseName "-" " " | title }}'
date: "{{ .Date }}"
draft: true
lastmod: "{{ .Date }}"
tags: ["Blog"]
categories: ["thinking"]
authors:
  - "ryluiiwan"
---
```

```shell
hugo new posts/blog.md
```

- 上传到 Git 仓库，Cloudflare 会自动部署

```shell
git add .   #将文件提交到暂存区
```

```shell
git commit -m "update"
```

```shell
git push
```

另外上传的时候有的时候出现：Git 报错` Failed to connect to github.com port 443`

✨ 记录一下解决方案: 查看自己电脑中的系统代理端口号，改一下`127.0.0.1后的端口号`

```shell
git config --global http.proxy 127.0.0.1:8087
```

## 📍 购买域名&Cloudflare 部署

域名购买我大概看了[GoDaddy](https://godaddy.com/)、[NameSilo](https://www.namesilo.com/)、[Cloudflare](https://www.cloudflare.com/)。因为这个字符串`ryluiiwan`我已经用了很久，所以选定了网域之后，对比了不同平台的价格
，选择了最便宜的[Cloudflare](https://www.cloudflare.com/)，一年$10.44。但`Cloudflare`不支持国内支付宝等支付方式，最后在闲鱼上找了一个 visa 代付，也算是成功解决了这个问题。

### Cloudflare Pages 构建博客

Cloudflare Pages 是 Cloudflare 推出的静态网站托管服务，可以直接连接 Github 仓库，完成自动化部署。
![创建pages](static/images/p1.jpg "Cloudflare pages创建")

### 添加 DNS 解析

### Reference

- [ChatGPT](https://chatgpt.com/)

- [Hugo + GitHub Action，搭建你的博客自动发布系统](https://www.pseudoyu.com/zh/2022/05/29/deploy_your_blog_using_hugo_and_github_action/)
